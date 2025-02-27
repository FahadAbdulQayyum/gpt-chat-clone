import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
GENAI_API_KEY = os.getenv("GEMINI_API_KEY")

# Check if the key exists
if not GENAI_API_KEY:
    st.error("API Key is missing! Please set GEMINI_API_KEY in .env file.")
else:
    genai.configure(api_key=GENAI_API_KEY)

    # Initialize the model
    # model = genai.GenerativeModel("gemini-pro")
    model = genai.GenerativeModel("gemini-1.5-pro")  # Or try "gemini-1.5-pro"

    st.title("Free GPT Chatbox")

    # User input field
    user_input = st.text_input("You:", "")

    if st.button("Send"):
        if user_input:
            response = model.generate_content(user_input)
            st.text_area("Bot:", response.text if response.text else "Sorry, I couldn't respond.", height=100)
