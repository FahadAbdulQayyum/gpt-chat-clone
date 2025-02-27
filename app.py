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
    model = genai.GenerativeModel("gemini-1.5-pro")  

    # App title
    st.title("Free GPT Chatbox")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # --- Floating Input Box ---
    # Use st.chat_input() for a persistent bottom input field
    user_input = st.chat_input("Type your message...")

    if user_input:
        # Display user message
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Generate response
        response = model.generate_content(user_input)
        bot_reply = response.text if response.text else "Sorry, I couldn't respond."

        # Display bot response
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})

        # Refresh UI to keep input box empty
        st.rerun()
