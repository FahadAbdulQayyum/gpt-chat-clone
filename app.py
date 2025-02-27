import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import time  

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
    user_input = st.chat_input("Type your message...")

    if user_input:
        # Append user message instantly
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Display chat history again (including user message)
        st.rerun()

    # Check if there is a new user message that needs a bot response
    if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
        # Show "Thinking..." while processing
        with st.chat_message("assistant"):
            loading_placeholder = st.empty()
            loading_placeholder.markdown("🔄 **Thinking...**")

        # Generate response
        response = model.generate_content(st.session_state.messages[-1]["content"])
        bot_reply = response.text if response.text else "Sorry, I couldn't respond."

        # Replace "Thinking..." with typing effect
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            typed_text = ""
            
            # Typing effect: Show response character by character
            for char in bot_reply:
                typed_text += char
                response_placeholder.markdown(typed_text + "▌")  # Cursor effect
                time.sleep(0.03)  # Adjust speed for realistic typing effect
            
            # Remove cursor after typing is done
            response_placeholder.markdown(typed_text)

        # Store bot response in chat history
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})

        # Refresh UI
        st.rerun()
