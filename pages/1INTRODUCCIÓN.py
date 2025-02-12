import streamlit as st
import pandas as pd

st.title("INTRODUCCIÓN AL DATASET")

data = {
    "Característica": [
        "Diabetes_binary 🩺", "HighBP ❤️‍🩹", "HighChol 🍔", "CholCheck 💉", "BMI ⚖️", 
        "Smoker 🚬", "Stroke 💔", "HeartDiseaseorAttack ❤️‍🩺", "PhysActivity 🏃‍♂️", 
        "Fruits 🍎", "Veggies 🥦", "HvyAlcoholConsump 🍷", "AnyHealthcare 🏥", 
        "NoDocbcCost 💸", "GenHlth 🏥", "MentHlth 🧠", "PhysHlth 💪", "DiffWalk 🚶‍♂️", 
        "Sex 🚹 / 🚺", "Age 👵👶", "Education 🎓", "Income 💰"
    ],
    "Descripción": [
        "0 = no diabetes, 1 = diabetes", 
        "0 = no high blood pressure, 1 = high blood pressure", 
        "0 = no high cholesterol, 1 = high cholesterol", 
        "0 = no cholesterol check in 5 years, 1 = yes cholesterol check in 5 years", 
        "Body Mass Index (range of values based on weight/height)", 
        "0 = no, 1 = yes (Have you smoked at least 100 cigarettes?)", 
        "0 = no stroke, 1 = yes stroke (ever told you had a stroke)", 
        "0 = no coronary heart disease, 1 = yes coronary heart disease", 
        "0 = no physical activity in past 30 days, 1 = yes physical activity", 
        "0 = no, 1 = yes (Consume fruit 1 or more times per day)", 
        "0 = no, 1 = yes (Consume vegetables 1 or more times per day)", 
        "0 = no, 1 = yes (Heavy alcohol consumption)", 
        "0 = no, 1 = yes (Any health care coverage, including insurance)", 
        "0 = no, 1 = yes (Couldn’t see a doctor due to cost)", 
        "General health rating (scale from 1 to 5, 1 = excellent to 5 = poor)", 
        "Days of poor mental health (scale from 1 to 30 days)", 
        "Days of physical illness or injury in past 30 days", 
        "0 = no, 1 = yes (Difficulty walking or climbing stairs)", 
        "0 = female, 1 = male", 
        "Age group (category from 18-24 to 80 or older)", 
        "Education level (scale from 1 to 6)", 
        "Income level (scale from 1 to 8)"
    ],
    "Tipo": [
        "Variable a predecir", "Categórica", "Categórica", "Categórica", "Numérica", 
        "Categórica", "Categórica", "Categórica", "Categórica", "Categórica", 
        "Categórica", "Categórica", "Categórica", "Categórica", "Categórica", 
        "Categórica", "Categórica", "Categórica", "Categórica", "Categórica", 
        "Categórica","Categórica"
    ]
}

df = pd.DataFrame(data)

# Mostrar la tabla en Streamlit
st.write("### El dataset contiene una serie de características relacionadas principalmente con la salud y los hábitos:")
st.dataframe(df)



