import os

from dotenv import load_dotenv

import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

print("API KEY:", API_KEY)

genai.configure(
    api_key=API_KEY
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def ask_llm(prompt):

    response = model.generate_content(prompt)

    return response.text