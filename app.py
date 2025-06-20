import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('home_price_model.pkl')

# App title
st.title("🏠 Home Price Prediction App")

# Input fields
st.header("Enter Property Details:")
area = st.number_input("Area (in sq. ft.)")
bedrooms = st.number_input("Number of Bedrooms", min_value=1, step=1)
age = st.number_input("Age of the House (in years)", min_value=0, step=1)

# Predict button
if st.button("Predict Price"):
    # Prepare input for prediction
    input_data = np.array([[area, bedrooms, age]])  # <-- Updated
    prediction = model.predict(input_data)
    st.success(f"🏡 Estimated Home Price: ₹{prediction[0]:,.2f}")
