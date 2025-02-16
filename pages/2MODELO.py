import streamlit as st
import pandas as pd
import torch
import torch.nn as nn
import numpy as np

# Definir la red neuronal
class DiabetesNN(nn.Module):
    def __init__(self, input_size):
        super(DiabetesNN, self).__init__()
        self.fc1 = nn.Linear(input_size, 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, 16)
        self.fc4 = nn.Linear(16, 1)
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()
        self.dropout = nn.Dropout(p=0.5)

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.relu(self.fc2(x))
        x = self.dropout(x)
        x = self.relu(self.fc3(x))
        x = self.fc4(x)
        x = self.sigmoid(x)
        return x

# Cargar el modelo entrenado
model = DiabetesNN(input_size=21)  # Asegúrate de que las características sean 21
try:
    model.load_state_dict(torch.load('rn_model.pth', map_location=torch.device('cpu')))
    model.eval()  # Modo de evaluación
except Exception as e:
    st.write(f"Error al cargar el modelo: {e}")

st.set_page_config(page_title="Cuestionario Gráfico", layout="wide")

# CSS para estilos y para centrar el contenido
st.markdown(
    """
    <style>
    @keyframes gradientMove {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .banner {
        background: linear-gradient(270deg, #34495e, #aab7b8, #839192, #34495e);
        background-size: 600% 600%;
        animation: gradientMove 10s ease infinite;
        color: white;
        padding: 30px;
        text-align: center;
        border-radius: 15px;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .question-container {
        background: linear-gradient(to bottom, #424949, #515a5a, #616a6b);
        padding: 15px;
        border-radius: 10px;
        margin: 8px 0;
        box-shadow: 0 4px 8px rgba(0,0,0,0.9);
        color: #ffffff;
        text-align: center;
    }
    .question-container h3 {
        font-size: 14px;
    }
    .centered-container {
         margin-left: auto;
         margin-right: auto;
         max-width: 800px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='banner'><h1>¡Conoce si tienes Diabetes!</h1><p>Selecciona las siguientes respuestas</p></div>", unsafe_allow_html=True)

# Diccionario para almacenar las respuestas
questions = {}

# Creamos las pestañas
tab1, tab2, tab3, tab4 = st.tabs(["Datos Personales", "Salud", "Estilo de Vida", "Generales"])

# TAB 1: Datos Personales (usando text_input para números)
with tab1:
    st.markdown('<div class="centered-container">', unsafe_allow_html=True)
    st.subheader("Datos Personales")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='question-container'><h3>¿Cuál es tu edad?</h3></div>", unsafe_allow_html=True)
        edad = st.slider("Ingresa tu edad", 18, 100, 60)
        questions["Edad"] = edad
        
        st.markdown("<div class='question-container'><h3>¿Cuál es tu peso (kg)?</h3></div>", unsafe_allow_html=True)
        peso = st.slider("Ingresa tu peso", 40,200, 80)
        questions["Peso"] = peso
    with col2:
        st.markdown("<div class='question-container'><h3>¿Cuál es tu altura (cm)?</h3></div>", unsafe_allow_html=True)
        altura = st.slider("Ingresa tu altura", 100,220, 150)
        questions["Altura"] = altura
    st.markdown('</div>', unsafe_allow_html=True)

# TAB 2: Salud (usando selectbox con placeholder)
with tab2:
    st.markdown('<div class="centered-container">', unsafe_allow_html=True)
    st.subheader("Salud")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='question-container'><h3>Califica tu salud del 1 al 5 (1: Excelente, 5: Mala)</h3></div>", unsafe_allow_html=True)
        califica = st.selectbox("Selecciona tu respuesta", ["Seleccione una opción", 1, 2, 3, 4, 5], key="califica")
        questions["Califica salud 1-5"] = califica
        
        st.markdown("<div class='question-container'><h3>¿Cuántos días en los últimos 30 no estuvo bien tu salud mental?</h3></div>", unsafe_allow_html=True)
        mental = st.selectbox("Selecciona tu respuesta", ["Seleccione una opción"] + list(range(0, 31)), key="mental")
        questions["Salud mental días"] = mental
    with col2:
        st.markdown("<div class='question-container'><h3>¿Cuántos días en los últimos 30 no estuvo bien tu salud física?</h3></div>", unsafe_allow_html=True)
        fisica = st.selectbox("Selecciona tu respuesta", ["Seleccione una opción"] + list(range(0, 31)), key="fisica")
        questions["Salud física días"] = fisica
    st.markdown('</div>', unsafe_allow_html=True)

# TAB 3: Estilo de Vida (usando selectbox para las opciones)
with tab3:
    st.markdown('<div class="centered-container">', unsafe_allow_html=True)
    st.subheader("Estilo de Vida")
    multiple_choice_questions = [
        "¿Tienes la presión arterial alta?",
        "¿Tienes el colesterol alto?",
        "¿Te has hecho exámenes de colesterol en los últimos 5 años?",
        "¿Has fumado más de 100 cigarrillos en toda tu vida?",
        "¿Has tenido accidentes cerebrovasculares?",
        "¿Tienes enfermedades coronarias?",
        "¿Has hecho actividad física en los últimos 30 días?",
        "¿Consumes al menos una fruta por día?",
        "¿Consumes vegetales al menos una vez al día?",
        "¿Eres un consumidor habitual de alcohol?",
        "¿Cuentas con un seguro médico?",
        "¿En el último año, necesitaste visitar al doctor pero no pudiste por el costo?"
    ]
    col1, col2 = st.columns(2)
    for i, q in enumerate(multiple_choice_questions):
        if i % 2 == 0:
            with col1:
                st.markdown(f"<div class='question-container'><h3>{q}</h3></div>", unsafe_allow_html=True)
                respuesta = st.selectbox("Selecciona una opción", ["Seleccione una opción", "Sí", "No"], key=f"multi_{i}")
                questions[q] = respuesta
        else:
            with col2:
                st.markdown(f"<div class='question-container'><h3>{q}</h3></div>", unsafe_allow_html=True)
                respuesta = st.selectbox("Selecciona una opción", ["Seleccione una opción", "Sí", "No"], key=f"multi_{i}")
                questions[q] = respuesta
    st.markdown('</div>', unsafe_allow_html=True)

# TAB 4: Generales
with tab4:
    st.markdown('<div class="centered-container">', unsafe_allow_html=True)
    st.subheader("Generales")
    col1, col2 = st.columns(2)
    with col1:
        
        st.markdown("<div class='question-container'><h3>¿Tienes dificultades para caminar o subir escaleras?</h3></div>", unsafe_allow_html=True)
        dificultades = st.selectbox("Selecciona una opción", ["Seleccione una opción", "Sí", "No"], key="dificultades")
        questions["Dificultades para subir escaleras"] = dificultades
        
        st.markdown("<div class='question-container'><h3>¿Cuál es tu nivel de ingresos anuales?</h3></div>", unsafe_allow_html=True)
        income_levels = {
            0: "Seleccione una opción",
            1: "Hasta €10K",
            2: "Hasta €15K",
            3: "Hasta €20K",
            4: "Hasta €25K",
            5: "Hasta €35K",
            6: "Hasta €50K",
            7: "Hasta €75K",
            8: "Más de €75K"
        }
        ingresos = st.selectbox(
            "Selecciona tu nivel de ingresos", 
            options=list(income_levels.keys()), 
            format_func=lambda x: income_levels[x], 
            key="ingresos"
        )
        questions["Nivel de ingresos"] = ingresos
    with col2:
        st.markdown("<div class='question-container'><h3>¿Cuál es tu género?</h3></div>", unsafe_allow_html=True)
        genero = st.selectbox("Selecciona una opción", ["Seleccione una opción", "Masculino", "Femenino"], key="genero")
        questions["Género"] = genero
        
        st.markdown("<div class='question-container'><h3>¿Cuál es tu nivel de educación?</h3></div>", unsafe_allow_html=True)
        education_levels = {
            0: "Seleccione una opción",
            1: "Nunca asistió a la escuela o solo jardín de infantes",
            2: "Grados 1 a 8 (Primaria)",
            3: "Grados 9 a 11 (Alguna escuela secundaria)",
            4: "Grado 12 o GED (Graduado de escuela secundaria)",
            5: "Universidad 1 a 3 años (Alguna universidad o escuela técnica)",
            6: "Universidad 4 años o más (Graduado universitario)"
        }
        educacion = st.selectbox(
            "Selecciona tu nivel de educación", 
            options=list(education_levels.keys()), 
            format_func=lambda x: education_levels[x], 
            key="educacion"
        )
        questions["Nivel de educación"] = educacion
    st.markdown('</div>', unsafe_allow_html=True)

# Función de validación para verificar que todas las preguntas hayan sido contestadas
def all_questions_answered(ans):
    # Validar campos de texto (Edad, Peso, Altura)
    for key in ["Edad", "Peso", "Altura"]:
        if not ans.get(key) or ans[key] == "":
            return False
        try:
            if int(ans[key]) <= 0:
                return False
        except:
            return False

    # Validar selectboxes de la pestaña Salud
    if ans["Califica salud 1-5"] == "Seleccione una opción":
        return False
    if ans["Salud mental días"] == "Seleccione una opción":
        return False
    if ans["Salud física días"] == "Seleccione una opción":
        return False

    # Validar cada pregunta de Estilo de Vida
    for q in multiple_choice_questions:
        if ans[q] == "Seleccione una opción":
            return False

    # Validar selectboxes de la pestaña Generales
    if ans["Dificultades para subir escaleras"] == "Seleccione una opción":
        return False
    if ans["Nivel de ingresos"] == 0:
        return False
    if ans["Género"] == "Seleccione una opción":
        return False
    if ans["Nivel de educación"] == 0:
        return False

    return True

# Función para calcular el BMI
def calcular_bmi(peso, altura):
    if peso and altura:
        try:
            peso_kg = float(peso)
            altura_m = float(altura) / 100  # Convertir altura de cm a m
            return peso_kg / (altura_m ** 2)
        except:
            return None
    return None

def age_category(age):
    if 18 <= age <= 24:
        return 1
    elif 25 <= age <= 29:
        return 2
    elif 30 <= age <= 34:
        return 3
    elif 35 <= age <= 39:
        return 4
    elif 40 <= age <= 44:
        return 5
    elif 45 <= age <= 49:
        return 6
    elif 50 <= age <= 54:
        return 7
    elif 55 <= age <= 59:
        return 8
    elif 60 <= age <= 64:
        return 9
    elif 65 <= age <= 69:
        return 10
    elif 70 <= age <= 74:
        return 11
    elif 75 <= age <= 79:
        return 12
    else:
        return 13

# Función para convertir respuestas "Sí" y "No" a 1 y 0
def convertir_respuesta(respuesta):
    return 1 if respuesta == "Sí" else 0

# Mostrar el botón de envío solo si todas las respuestas son válidas
if all_questions_answered(questions):
    if st.button("Enviar Respuestas"):
        # Calcular BMI
        bmi = calcular_bmi(questions["Peso"], questions["Altura"])
        edad_rango = age_category(int(questions["Edad"]))
        
        # Crear el DataFrame con las respuestas
        data = {
            'HighBP': convertir_respuesta(questions["¿Tienes la presión arterial alta?"]),
            'HighChol': convertir_respuesta(questions["¿Tienes el colesterol alto?"]),
            'CholCheck': convertir_respuesta(questions["¿Te has hecho exámenes de colesterol en los últimos 5 años?"]),
            'BMI': bmi,
            'Smoker': convertir_respuesta(questions["¿Has fumado más de 100 cigarrillos en toda tu vida?"]),
            'Stroke': convertir_respuesta(questions["¿Has tenido accidentes cerebrovasculares?"]),
            'HeartDiseaseorAttack': convertir_respuesta(questions["¿Tienes enfermedades coronarias?"]),
            'PhysActivity': convertir_respuesta(questions["¿Has hecho actividad física en los últimos 30 días?"]),
            'Fruits': convertir_respuesta(questions["¿Consumes al menos una fruta por día?"]),
            'Veggies': convertir_respuesta(questions["¿Consumes vegetales al menos una vez al día?"]),
            'HvyAlcoholConsump': convertir_respuesta(questions["¿Eres un consumidor habitual de alcohol?"]),
            'AnyHealthcare': convertir_respuesta(questions["¿Cuentas con un seguro médico?"]),
            'NoDocbcCost': convertir_respuesta(questions["¿En el último año, necesitaste visitar al doctor pero no pudiste por el costo?"]),
            'GenHlth': questions["Califica salud 1-5"],
            'MentHlth': questions["Salud mental días"],
            'PhysHlth': questions["Salud física días"],
            'DiffWalk': convertir_respuesta(questions["Dificultades para subir escaleras"]),
            'Sex': 1 if questions["Género"] == "Masculino" else 0,
            'Age': int(questions["Edad"]),
            'Education': questions["Nivel de educación"],
            'Income': questions["Nivel de ingresos"]
        }
        
        # Crear DataFrame
        df = pd.DataFrame([data])

        st.subheader("RESUMEN DE RESPUESTAS")
        st.write(df)


        input_tensor = torch.tensor(np.array(df), dtype=torch.float32).unsqueeze(0)  # Añadir batch dimension
    
        with torch.no_grad():
            prediction = model(input_tensor)
            prediction_value = prediction.item()  # Obtener el valor de la predicción
            st.subheader(f"PREDICCIÓN: {prediction_value:.4f}")
            if prediction_value >= 0.5:
                st.subheader("¡Probabilidad alta de diabetes!")
            else:
                st.subheader("¡Probabilidad baja de diabetes!")
        
else:
    st.info("Por favor, completa **todas** las respuestas para poder enviar el formulario.")

