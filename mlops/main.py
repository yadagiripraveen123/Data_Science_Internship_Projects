import streamlit as st
import numpy as np
from pickle import load
import sklearn

st.title(":blue[Medical Insurance Prediction]")
st.subheader("Given the Required features for Predicting the Medical Insurance")

st.text("""Health insurance is important because cost towards good medical facilities and hospitalisation can be financially stressful. 
With rising medical expenses, a health insurance cover can provide the added protection you need.Insurance plans are  beneficial to anyone 
looking to protect their family, assets/property and themselves from financial risk/losses: Insurance plans will help you pay for medical 
emergencies, hospitalisation, contraction of any illnesses and treatment, and medical care required in the future.""")



scaler = load(open(r"C:\Users\yadag\OneDrive\Desktop\Internship_Projects\mlops\resources\standard_scaler.pkl",'rb'))
ohe = load(open(r"C:\Users\yadag\OneDrive\Desktop\Internship_Projects\mlops\resources\ohe_encoder.pkl",'rb'))
gbdt_model = load(open(r"C:\Users\yadag\OneDrive\Desktop\Internship_Projects\mlops\resources\gbdt_model.pkl",'rb'))

age = st.text_input('Age', placeholder='Enter the age')
bmi = st.text_input('BMI', placeholder='Enter the BMI')
children = st.text_input('Children', placeholder='Enter number of children')
smoker = st.selectbox('Smoker', ['yes', 'no'])
st.write('You selected:', smoker)

btn_click = st.button('Predict')

if btn_click:
    if not (age and bmi and children):
        st.error('Age, BMI and Children must be numbers')
    elif  smoker not in ['yes', 'no']:
        st.error('Invalid input')
    else:
        # Convert input to a numpy array
        num = np.array([float(age), float(bmi), float(children)]).reshape(1,-1)
        # rescaling the numerical features
        num_rescaled = scaler.transform(num)
        # Encode categorical features
        cat = np.array([[smoker]])
        cat_transformed = ohe.transform(cat)
        # Combine the numerical and categorical features
        query_transformed = np.concatenate([num_rescaled, cat_transformed], axis=1)
        # Make prediction
        pred = np.exp(gbdt_model.predict(query_transformed))
        # Show prediction result
        st.success(f'The predicted insurance cost is {pred[0]:.2f} rupees.')