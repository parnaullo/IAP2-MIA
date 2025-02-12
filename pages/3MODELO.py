
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import RobustScaler
import pickle
import joblib
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


df = pd.read_csv("datos_limpios.csv")
lista = ["Accident_Final","Driver_Experience"]
df = df.drop(lista,axis=1)

with st.sidebar:
    
    # Mostrar los nombres de los integrantes
    st.subheader("Desarrolladores:")
    st.write("- ALBERTO GARCÍA")
    st.write("- PABLO ARNAU")
    st.write("- JAIRO NAVARRO")




st.header("Introduce tu valor a predecir")

col1, col2 = st.columns(2)

with col1:
		Weather = st.selectbox("Weather", ['Clear','Rainy', 'Foggy','Snowy','Stormy'])
		Road_type = st.selectbox("Road_type", ['Highway','City Road', 'Rural Road','Mountain Road'])
		Time_of_day = st.selectbox("Time_of_day", ['Afternoon','Evening', 'Morning','Night'])
		Traffic_Density = st.number_input("Traffic_Density", 0, 2, 0)
		Speed_Limit = st.number_input("Enter Speed_Limit", 30, 120, 60)
		Number_of_Vehicles = st.number_input("Enter number of vehicles involved", 1, 14, 7)

with col2:
		
		Road_Condition = st.selectbox("Road_Condition", ['Dry','Icy', 'Wet','Under Construction'])
		Vehicle_Type = st.selectbox("Vehicle_Type", ['Car','Truck', 'Motorcycle','Bus'])
		Driver_Age = st.slider("Enter your Age", 18, 69, 44)
		Road_Light_Condition = st.selectbox("Road_Light_Condition", ['Artificial Light','Daylight','No Light'])
		Driver_Alcohol = st.radio("Consumed alcohol",["Yes", "No"])



with st.expander("Your selected options"):
		so = {"Weather":Weather,
		"Road_Type":Road_type, "Time_of_Day":Time_of_day, "Traffic_Density":Traffic_Density,
		"Speed_Limit":Speed_Limit, "Number_of_Vehicles":Number_of_Vehicles, "Driver_Alcohol":Driver_Alcohol,
		"Road_Condition":Road_Condition,"Vehicle_Type":Vehicle_Type, "Driver_Age":Driver_Age,
		"Road_Light_Condition":Road_Light_Condition}


st.write(so)


def boton_pulsado(df,so):
	if so['Driver_Alcohol'] == 'Yes':
		so['Driver_Alcohol']= 1
	else: so['Driver_Alcohol'] = 0
	add = pd.DataFrame([so])
	df = pd.concat([df,add], ignore_index=True)
	st.dataframe(df)
	df_encoded=pd.get_dummies(df,drop_first=True)
	scaler=RobustScaler()
	columns=['Speed_Limit','Number_of_Vehicles','Driver_Age']
	df_encoded[columns] = scaler.fit_transform(df_encoded[columns])
	st.dataframe(df_encoded)
	model = joblib.load('modelo_accidentes.joblib') 
	X_821 = df_encoded.iloc[821:822]
	st.dataframe(X_821)
	prediccion = model.predict(X_821)
	st.write(prediccion)
	return df_encoded

# Crear un botón
if st.button('Submit'):
	boton_pulsado(df,so)




















