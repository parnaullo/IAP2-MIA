import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


df = pd.read_csv("diabetes_binary_5050split_health_indicators_BRFSS2015.csv")
st.set_page_config(page_title="EDA", layout="wide")

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
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='banner'><h1>Análisis Exploratorio de los Datos</h1><p></p></div>", unsafe_allow_html=True)

st.markdown("""
    <h3 style="
        text-align: left; 
        font-size: 28px;
        font-weight: bold;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
    ">
        Características del Set de Datos para la predicción de Diabetes
    </h3>
""", unsafe_allow_html=True)

st.write("""Este dataset contiene información sobre factores de riesgo y comportamientos relacionados con la salud, como presión arterial, colesterol, actividad física, dieta, acceso a atención médica y más. Estas características son útiles para analizar y predecir el riesgo de enfermedades crónicas, como la diabetes, y para identificar patrones de comportamiento relacionados con la salud. Cada columna tiene un propósito específico y está diseñada para capturar información relevante sobre el estilo de vida y la salud de las personas.""")



descripciones = {
    "HighBP ❤️‍🩹": """**Descripción:** Indica si la persona tiene presión arterial alta.  
**Valores:**  
- 1: Sí.  
- 0: No.  
**Relevancia:** La presión arterial alta es un factor de riesgo importante para enfermedades cardiovasculares y diabetes.""",
    "HighChol 🍔": """**Descripción:** Indica si la persona tiene colesterol alto.  
**Valores:**  
- 1: Sí.  
- 0: No.  
**Relevancia:** El colesterol alto está asociado con un mayor riesgo de enfermedades cardíacas y accidentes cerebrovasculares.""",
    "CholCheck 💉": """**Descripción:** Indica si la persona se ha realizado un chequeo de colesterol en los últimos 5 años.  
**Valores:**  
- 1: Sí.  
- 0: No.  
**Relevancia:** Muestra si la persona está al tanto de su nivel de colesterol, lo cual es importante para la prevención de enfermedades.""",
    "BMI ⚖️": """**Descripción:** Es una medida que relaciona el peso y la altura de una persona para determinar si tiene un peso saludable.  
**Fórmula:** BMI = peso (kg) / (altura (m))^2.  
**Valores:** Número decimal (por ejemplo, 24.5).  
**Relevancia:** Un BMI alto está asociado con un mayor riesgo de diabetes, enfermedades cardíacas y otras condiciones de salud.""",
    "Smoker 🚬": """**Descripción:** Indica si la persona ha fumado más de 100 cigarrillos en toda su vida.  
**Valores:**  
- 1: Sí.  
- 0: No.  
**Relevancia:** Fumar es un factor de riesgo importante para enfermedades respiratorias, cardiovasculares y cáncer.""",
    "Stroke 💔": """**Descripción:** Indica si la persona ha sufrido un accidente cerebrovascular.  
**Valores:**  
- 1: Sí.  
- 0: No.  
**Relevancia:** Los accidentes cerebrovasculares están relacionados con la presión arterial alta, el colesterol alto y otros factores de riesgo.""",
    "HeartDiseaseorAttack ❤️‍🩺": """**Descripción:** Indica si la persona ha tenido una enfermedad coronaria o un ataque al corazón.  
**Valores:**  
- 1: Sí.  
- 0: No.  
**Relevancia:** Las enfermedades cardíacas son una de las principales causas de muerte y están relacionadas con la diabetes y otros factores de riesgo.""",
    "PhysActivity 🏃‍♂️": """**Descripción:** Indica si la persona ha realizado actividad física en los últimos 30 días.  
**Valores:**  
- 1: Sí.  
- 0: No.  
**Relevancia:** La actividad física reduce el riesgo de enfermedades crónicas como la diabetes y las enfermedades cardíacas.""",
    "Fruits 🍎": """**Descripción:** Indica si la persona consume al menos una fruta por día.  
**Valores:**  
- 1: Sí.  
- 0: No.  
**Relevancia:** Una dieta rica en frutas está asociada con un menor riesgo de enfermedades crónicas.""",
    "Veggies 🥦 ": """**Descripción:** Indica si la persona consume vegetales al menos una vez al día.  
**Valores:**  
- 1: Sí.  
- 0: No.  
**Relevancia:** El consumo de vegetales es importante para una dieta saludable y la prevención de enfermedades.""",
    "HvyAlcoholConsump 🍷": """**Descripción:** Indica si la persona es un consumidor habitual de alcohol en grandes cantidades.  
**Valores:**  
- 1: Sí.  
- 0: No.  
**Relevancia:** El consumo excesivo de alcohol está relacionado con problemas de salud como enfermedades hepáticas y cardiovasculares.""",
    "AnyHealthcare 🏥": """**Descripción:** Indica si la persona tiene acceso a un seguro médico.  
**Valores:**  
- 1: Sí.  
- 0: No.  
**Relevancia:** El acceso a atención médica es crucial para la prevención y el tratamiento de enfermedades.""",
    "NoDocbcCost 💸": """**Descripción:** Indica si la persona necesitó visitar al médico en el último año pero no pudo hacerlo debido al costo.  
**Valores:**  
- 1: Sí.  
- 0: No.  
**Relevancia:** Muestra barreras económicas para el acceso a la atención médica.""",
    "GenHlth 🏥": """**Descripción:** Es una autoevaluación de la salud general de la persona en una escala del 1 al 5.  
**Valores:**  
- 1: Excelente.  
- 2: Muy buena.  
- 3: Buena.  
- 4: Regular.  
- 5: Mala.  
**Relevancia:** La percepción de la salud general es un indicador importante del bienestar.""",
    "MentHlth 🧠": """**Descripción:** Número de días en los últimos 30 en los que la persona sintió que su salud mental no estuvo bien.  
**Valores:** Entero entre 0 y 30.  
**Relevancia:** La salud mental es un componente clave del bienestar general.""",
    "PhysHlth 💪": """**Descripción:** Número de días en los últimos 30 en los que la persona sintió que su salud física no estuvo bien.  
**Valores:** Entero entre 0 y 30.  
**Relevancia:** La salud física está relacionada con la capacidad para realizar actividades diarias.""",
    "DiffWalk 🚶‍♂️": """**Descripción:** Indica si la persona tiene dificultades para caminar o subir escaleras.  
**Valores:**  
- 1: Sí.  
- 0: No.  
**Relevancia:** Puede ser un indicador de problemas de movilidad o enfermedades crónicas.""",
    "Sex 🚹 / 🚺": """**Descripción:** Género de la persona.  
**Valores:**  
- 1: Masculino.  
- 0: Femenino.  
**Relevancia:** Algunas enfermedades tienen diferentes prevalencias según el género.""",
    "Age 👵👶": """**Descripción:** Edad de la persona.  
**Valores:** Entero (por ejemplo, 30).  

**1:** 18 a 24 años

**2:** 25 a 29 años

**3:** 30 a 34 años

**4:** 35 a 39 años

**5:** 40 a 44 años

**6:** 45 a 49 años

**7:** 50 a 54 años

**8:** 55 a 59 años

**9:** 60 a 64 años

**10:** 65 a 69 años

**11:** 70 a 74 años

**12:** 75 a 79 años

**13:** Mayores de 79 años

**Relevancia:** La edad es un factor de riesgo importante para muchas enfermedades crónicas.""",
    "Education 🎓": """**Descripción:** Nivel de educación de la persona.  
**Valores:**  
- 1: Nunca asistió a la escuela o solo jardín de infantes.  
- 2: Grados 1 a 8 (Primaria).  
- 3: Grados 9 a 11 (Alguna escuela secundaria).  
- 4: Grado 12 o GED (Graduado de escuela secundaria).  
- 5: Universidad 1 a 3 años (Alguna universidad o escuela técnica).  
- 6: Universidad 4 años o más (Graduado universitario).  
**Relevancia:** El nivel de educación puede influir en el acceso a información sobre salud y hábitos saludables.""",
    "Income 💰": """**Descripción:** Nivel de ingresos anuales de la persona.  
**Valores:**  
- 1: <€10K.  
- 2: <€15K.  
- 3: <€20K.  
- 4: <€25K.  
- 5: <€35K.  
- 6: <€50K.  
- 7: <€75K.  
- 8: €75K+.  
**Relevancia:** Los ingresos pueden afectar el acceso a atención médica y hábitos de vida saludables."""
}




descripciones_items = list(descripciones.items())


for i in range(0, len(descripciones_items), 3):
    cols = st.columns(3)
    for j, (columna, descripcion) in enumerate(descripciones_items[i:i+3]):
        with cols[j]:
            with st.expander(columna):
                st.markdown(descripcion)
                
st.dataframe(df)

with st.expander("Ver descripción estadísticas del DataFrame"):
    st.write(df.describe())
    

with st.expander("Conteo de valores duplicados"):
    st.write(df.duplicated().sum())
    st.write("Estos valores han sido eliminados para el entrenamiento del modelo")
    
with st.expander("Validación de valores nulos"):
    st.write(df.isnull().mean()*100)
    st.write("Este dataset no cuenta con valores nulos")
    
with st.expander("Aseguramos que los valores sean formato INT"):
    st.code("""
        cols = ["Diabetes_binary","HighBP", "HighChol", "CholCheck", "Smoker", "Stroke", 
               "HeartDiseaseorAttack", "PhysActivity", "Fruits", "Veggies", 
               "HvyAlcoholConsump", "AnyHealthcare", "NoDocbcCost", 
               "DiffWalk", "Sex","GenHlth", "MentHlth", "PhysHlth", "Age", "Education", "Income",'BMI']
df[cols] = df[cols].astype(int)""")
    
st.markdown("""
    <h3 style="
        text-align: left; 
        font-size: 28px;
        font-weight: bold;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
    ">
        Análisis Univariante del Set de Datos
    </h3>
""", unsafe_allow_html=True)




col1, col2 = st.columns(2)


with col1:

    chart_type_hist = st.radio('Selecciona el tipo de gráfico para visualizaciones', ['Histogram', 'Scatter'])


    column_hist = st.selectbox('Selecciona una columna para visualizar', 
                               ['BMI', 'MentHlth', 'PhysHlth', 'Age', 'Education', 'Income'])


    if chart_type_hist == 'Histogram':
        fig_hist = px.histogram(df, x=column_hist, marginal='rug', title=f'Distribución de {column_hist}')
    elif chart_type_hist == 'Scatter':
        fig_hist = px.scatter(df, x=column_hist, title=f'Distribución de {column_hist}')


    st.plotly_chart(fig_hist)


with col2:

    chart_type_pie = st.radio('Selecciona el tipo de gráfico para visualizaciones de características binarias', ['Pastel', 'Barras'])


    column_pie = st.selectbox('Selecciona una característica binaria para visualizar', 
                              ['HighBP', 'HighChol', 'CholCheck', 'Smoker',
                               'Stroke', 'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies',
                               'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost', 'GenHlth',
                               'DiffWalk', 'Sex', 'Diabetes_binary'])


    if chart_type_pie == 'Pastel':
        fig_pie = px.pie(df, names=column_pie, title=f'Distribución de {column_pie}')
    
    elif chart_type_pie == 'Barras':

        pie_grouped = df.groupby(column_pie).size().reset_index(name='count')
        pie_grouped['Percentage'] = pie_grouped['count'] / pie_grouped['count'].sum() * 100
        fig_pie = px.bar(pie_grouped, x=column_pie, y='Percentage', title=f'Distribución de {column_pie}', labels={'Percentage': 'Percentage'})

    st.plotly_chart(fig_pie)
    
st.markdown("""
    <h3 style="
        text-align: left; 
        font-size: 28px;
        font-weight: bold;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
    ">
        Análisis Bivariante del set de Datos
    </h3>
""", unsafe_allow_html=True)

gender_filter = st.radio('Selecciona el género', ['Hombre', 'Mujer'])


if gender_filter == 'Hombre':
    data_filtered = df[df['Sex'] == 1]
else:
    data_filtered = df[df['Sex'] == 0]


diabetes_filter = st.radio('Selecciona el estado de diabetes', ['Diabético', 'No Diabético', 'Todos'])


if diabetes_filter == 'Diabético':
    data_filtered = data_filtered[data_filtered['Diabetes_binary'] == 1]
elif diabetes_filter == 'No Diabético':
    data_filtered = data_filtered[data_filtered['Diabetes_binary'] == 0]


columns = ['Age', 'Education', 'Income', 'BMI', 'MentHlth', 'PhysHlth']
group_column = st.selectbox('Selecciona una columna para agrupar', columns)


diabetic_grouped = data_filtered.groupby(group_column).size().reset_index(name='count')
diabetic_grouped['Percentage'] = diabetic_grouped['count'] / diabetic_grouped['count'].sum() * 100


fig = px.bar(diabetic_grouped, x=group_column, y='Percentage',
             labels={'Percentage': 'Percentage of Diabetics'},
             title=f'Percentage of Diabetics by {group_column.capitalize()} ({gender_filter}, {diabetes_filter})')

st.plotly_chart(fig)


# Definir las columnas específicas que quieres incluir
columnas = ['HighBP', 'HighChol', 'BMI', 'GenHlth', 'DiffWalk', 'Sex', 'Age', 'Diabetes_binary']  # Sustituye por las columnas que deseas

# Filtrar el DataFrame para mantener solo las columnas seleccionadas
filtered_df = df[columnas]

# Filtrar solo las columnas numéricas
numeric_filtered_df = filtered_df.select_dtypes(include=['number'])

# Calcular la matriz de correlaciones de Spearman
spearman_corr = numeric_filtered_df.corr(method='spearman')

# Crear una figura de Plotly para la matriz de correlaciones
fig = go.Figure(data=go.Heatmap(
    z=spearman_corr.values,
    x=spearman_corr.columns,
    y=spearman_corr.columns,
    colorscale='RdBu',
    zmin=-1, zmax=1,
    text=spearman_corr.values,
    texttemplate='%{text:.2f}',
    textfont={"size":14},
    showscale=True
))

# Título de la aplicación
st.markdown("""
    <h3 style="
        text-align: left; 
        font-size: 28px;
        font-weight: bold;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
    ">
        Matriz de Correlación
    </h3>
""", unsafe_allow_html=True)

# Mostrar el gráfico en la aplicación
st.plotly_chart(fig)