import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
# GENAI_API_KEY = os.getenv("GEMINI_API_KEY")

# genai.configure(api_key="YOUR_GEMINI_API_KEY")
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

models = genai.list_models()
for model in models:
    print(model.name)





# import google.generativeai as genai

# genai.configure(api_key="YOUR_GEMINI_API_KEY")

# models = genai.list_models()
# for model in models:
#     print(model.name)















# import requests

# # Define the prompt to be sent
# prompt = 'Please generate a simple blog post according to this title "What is CHATGPT"'

# # Enter E-mail to generate API
# api_key = 'Enter your E-mail Address to get the free ChatGPT API'

# # Define the default model if none is specified
# default_model = 'gpt-3.5-turbo'

# # Uncomment the model you want to use, and comment out the others
# # model = 'gpt-4'
# # model = 'gpt-4-32k'
# # model = 'gpt-3.5-turbo-0125'
# model = default_model

# # Build the URL to call
# api_url = f'http://195.179.229.119/gpt/api.php?prompt={requests.utils.quote(prompt)}&api_key={requests.utils.quote(api_key)}&model={requests.utils.quote(model)}'

# try:
#     # Execute the HTTP request
#     response = requests.get(api_url)
#     response.raise_for_status()  # Raise an error for bad HTTP status codes

#     # Parse and print the response
#     data = response.json()
#     print(data)

# except requests.RequestException as e:
#     # Print any errors
#     print(f'Request Error: {e}')