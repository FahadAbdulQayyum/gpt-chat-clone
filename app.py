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




















# import streamlit as st
# import google.generativeai as genai

# # Configure the Gemini API key
# GENAI_API_KEY = "AIzaSyCulkoJYR6VoCHxANpwoXLLuV07PWxQ4AA"
# # GENAI_API_KEY = "YOUR_GEMINI_API_KEY"
# genai.configure(api_key=GENAI_API_KEY)

# # Initialize the model
# model = genai.GenerativeModel("gemini-pro")

# st.title("Free GPT Chatbox")

# # User input field
# user_input = st.text_input("You:", "")

# if st.button("Send"):
#     if user_input:
#         response = model.generate_content(user_input)
#         st.text_area("Bot:", response.text if response.text else "Sorry, I couldn't respond.", height=100)












# # import streamlit as st
# # import requests

# # API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-small"
# # HEADERS = {"Authorization": "Bearer YOUR_HUGGINGFACE_API_KEY"}

# # def query(payload):
# #     response = requests.post(API_URL, headers=HEADERS, json=payload)
# #     return response.json()

# # st.title("Free GPT Chatbox")
# # user_input = st.text_input("You:", "")

# # if st.button("Send"):
# #     output = query({"inputs": user_input})
# #     st.text_area("Bot:", output.get("generated_text", "Sorry, I couldn't respond."), height=100)




























# # # import streamlit as st

# # # st.title("My First Streamlit App")
# # # st.write("Hello, world!")
# # # name = st.text_input("Enter your name:")
# # # if name:
# # #     st.write(f"Hello, {name}!")