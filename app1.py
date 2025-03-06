import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import time  
import json

# Load environment variables
load_dotenv()
GENAI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=GENAI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")

# Unit categories and their respective units
unit_categories = {
    "Length": ["Meters", "Kilometers", "Miles", "Feet", "Inches"],
    "Mass": ["Grams", "Kilograms", "Pounds", "Ounces"],
    "Time": ["Seconds", "Minutes", "Hours", "Days"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Speed": ["Meters per second", "Kilometers per hour", "Miles per hour"],
    "Area": ["Square meters", "Square kilometers", "Acres", "Hectares"],
    "Volume": ["Liters", "Milliliters", "Cubic meters", "Gallons"],
    "Energy": ["Joules", "Calories", "Kilowatt-hours"],
    "Pressure": ["Pascals", "Bars", "PSI"],
    "Frequency": ["Hertz", "Kilohertz", "Megahertz", "Gigahertz"],
    "Digital Storage": ["Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Terabytes"],
    "Data Transfer Rate": ["Bits per second", "Kilobits per second", "Megabits per second", "Gigabits per second"],
    "Fuel Economy": ["Kilometers per liter", "Miles per gallon"],
    "Plane Angle": ["Degrees", "Radians"],
}

# Streamlit UI
st.title("🔢 AI-Powered Unit Converter")

# Category Selection
category = st.selectbox("Select Category", list(unit_categories.keys()))
units = unit_categories[category]

# Input Section
col1, col2, col3 = st.columns([2, 1, 2])
with col1:
    value = st.number_input("Enter Value", min_value=0.0, step=0.01)
    from_unit = st.selectbox("From Unit", units)
with col2:
    st.markdown("### =")
with col3:
    to_unit = st.selectbox("To Unit", units)

if st.button("Convert"):
    with st.spinner("🔄 Calculating..."):
        time.sleep(1)  # Simulate processing delay

        # Generate conversion request
        prompt = f"""
        Convert {value} {from_unit} to {to_unit}. 
        Provide the response in strict JSON format with two keys:
        1. "text": The conversion result as a string.
        2. "formula": The formula used for conversion.
        Example output: {{"text": "0.0166667", "formula": "Divide the time value by 60"}}
        """

        response = model.generate_content(prompt)
        
        # Debugging response
        # print("Raw response:", response)
        print("Raw response:", response.text)

        try:
            # Parse JSON response safely
            response_json = json.loads(response.text or "{}")
            result = response_json.get("text", "Couldn't calculate.")
            formula = response_json.get("formula", "Formula unavailable.")
        except (json.JSONDecodeError, AttributeError):
            result = "Couldn't calculate."
            formula = "Formula unavailable."

    # Display result
    st.write(f"### {value} {from_unit} = {result} {to_unit}")
    st.info(f"Formula: {formula}")
