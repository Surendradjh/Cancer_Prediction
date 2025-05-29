import streamlit as st
st.title("Cancer Detection around 50%")
age = st.number_input('Age', )
gender = st.selectbox('Gender', ['Male', 'Female'])
tumor_size = st.number_input('Tumor Size (in mm)')
tumor_grade = st.selectbox('Tumor Grade', ['High','Low','Medium'])
symptoms_severity = st.selectbox('Symptoms_severity',['Moderate','Severe','Mild'])
family_history = st.selectbox('Family History', ['Yes', 'No'])
smoking_history = st.selectbox('Smoking History', ['Non-Smoker', 'Former Smoker', 'Current Smoker'])
alcohol_consumption = st.selectbox('Alcohol Consumption', ['Low', 'Occasionally', 'Regularly'])
exercise_frequency = st.selectbox('Exercise Frequency', ['Rarely', 'Regularly', 'Occasionally'])

import pickle

with open(r"cancer_prediction.pkl",'rb') as file:
    model=pickle.load(file) 

import pandas as pd 
d = pd.DataFrame([[age, gender, tumor_size, tumor_grade, symptoms_severity, family_history, smoking_history, alcohol_consumption, exercise_frequency]], 
                 columns=['Age', 'Gender', 'Tumor_Size', 'Tumor_Grade', 'Symptoms_Severity', 'Family_History', 'Smoking_History', 'Alcohol_Consumption', 'Exercise_Frequency'])
if st.button('Predict'):
    st.subheader("Patient details")
    st.write(d)
    st.subheader("Result")
    try:
        result = model.predict(d)
        if result==0:
            st.success('Cancer is Negative')
        elif result == 1:
            st.success("Cancer is Positive")
        else:
            st.warning("Error in the prediction")
    except Exception as e:
        st.warning(e)
