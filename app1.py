import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import time  

# Load environment variables
load_dotenv()
GENAI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=GENAI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")

# Streamlit UI
st.title("🔢 Unit Converter using AI")

# Input Section
value = st.number_input("Enter Value", min_value=0.0, step=0.01)
from_unit = st.selectbox("From Unit", ["Meters", "Kilometers", "Miles", "Feet", "Inches", "Grams", "Kilograms", "Pounds", "Ounces"])
to_unit = st.selectbox("To Unit", ["Meters", "Kilometers", "Miles", "Feet", "Inches", "Grams", "Kilograms", "Pounds", "Ounces"])

if st.button("Convert"):
    with st.spinner("🔄 Calculating..."):
        time.sleep(1)  # Simulate processing delay

        # Generate conversion request
        prompt = f"Convert {value} {from_unit} to {to_unit}. Provide only the numeric result."
        response = model.generate_content(prompt)
        result = response.text if response.text else "Couldn't calculate."

    st.write(f"### Result: {value} {from_unit} = {result} {to_unit}")
