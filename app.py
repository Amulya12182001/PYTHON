import streamlit as st
import json
import numpy as np
import pickle

# Load the inputs from the JSON file
with open('inputs.json', 'r') as f:
    inputs = json.load(f)

# Load the model (replace 'model.pkl' with your actual model file)
# with open('model.pkl', 'rb') as f:
#     model = pickle.load(f)

# Dummy function to simulate prediction (replace with actual model prediction)
def predict_charges(age, bmi, children, smoker, sex, region):
    # Example of dummy prediction logic
    charges = age * bmi + children * 1000
    if smoker == "yes":
        charges += 20000
    if sex == "male":
        charges += 500
    if region in ["northeast", "northwest"]:
        charges += 300
    return charges

# Streamlit app
st.title("Insurance Charges Prediction")

st.sidebar.header("Input Parameters")

age = st.sidebar.slider("Age", inputs["age"][0], inputs["age"][1], 25)
bmi = st.sidebar.slider("BMI", inputs["bmi"][0], inputs["bmi"][1], 22.0)
children = st.sidebar.slider("Children", inputs["children"][0], inputs["children"][1], 1)
smoker = st.sidebar.selectbox("Smoker", inputs["smoker"])
sex = st.sidebar.selectbox("Sex", inputs["sex"])
region = st.sidebar.selectbox("Region", inputs["region"])

# Predict charges
if st.sidebar.button("Predict"):
    charges = predict_charges(age, bmi, children, smoker, sex, region)
    st.write(f"Predicted Charges: ${charges:.2f}")
