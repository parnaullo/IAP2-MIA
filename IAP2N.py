import streamlit as st

icono1 = "⬇️"
icono = "📂"
icono2 = "🩺"
icono3= "📊"

st.markdown(f"<h1 style='text-align: center''><span>{icono2}</span> DIABETES HEALTH INDICATORS DATASET <span>{icono3}</span></h1><br>", unsafe_allow_html=True)


import streamlit as st

# Incrementar el tamaño de la letra directamente con HTML y CSS en st.markdown
st.markdown('''
    <p style="font-size: 20px;">
        La DIABETES una enfermedad prolongada (crónica) en la cual el cuerpo no puede regular la cantidad de azúcar en la sangre.
        Es, además, una de las enfermedades no contagiosas más frecuentes del mundo. En España afecta a casi 6 millones de personas. 
        Los datos recogidos por las encuestas nacionales y europeas de salud reflejan una tasa de 7,51 de cada 100 personas.<br>
        <br>En este proyecto vamos a entrenar un modelo para que sea capaz de predecir la presencia de la enfermedad o no dependiendo de una serie de variables que recogen la información sobre cada muestra.
    </p><br>
''', unsafe_allow_html=True)


url = "https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset/data?select=diabetes_binary_5050split_health_indicators_BRFSS2015.csv"


st.markdown(f"<h3 style='text-align: center;'>DATASET LINK {icono1}</h3>", unsafe_allow_html=True)

st.markdown(f'<div style="text-align: center;"><a href="{url}" target="_blank" style="font-size: 100px;">{icono}</a></div>', unsafe_allow_html=True)


st.markdown(
    """
    <style>
    .css-1d391kg {  # Sidebar container class
        display: flex;
        flex-direction: column;
        height: 100vh;
    }
    .css-1d391kg > div:last-child {
        margin-top: auto;
    }
    .dev-footer {
        margin-top: auto;
        padding-top: 400px;
        padding-bottom: 20px;
        font-size: 20px;
        text-align: center;
        border-top: 1px solid #ddd;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Crear la barra lateral
with st.sidebar:

    # Nombres de los desarrolladores en la parte inferior
    st.markdown('<div class="dev-footer"><strong>Desarrolladores:</strong><br>Alberto García<br>Jairo Navarro<br>Pablo Arnau</div>', unsafe_allow_html=True)
