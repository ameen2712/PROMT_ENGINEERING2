from google import genai
from google.genai import types
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

llm = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


st.title("Angry BOT 😠 ")

user_input = st.text_input("Enter here")

user_check = st.table()

user1= st.audio
submit = st.button("Submit")


print("I AM WORKING")

def model_response(user_input):
    response = llm.models.generate_content(
        model="gemini-2.0-flash",
        contents=types.Part.from_text(text=user_input),
        config=types.GenerateContentConfig(
            temperature=1,
            system_instruction="Classify the user input and answer in a rude way no problem what ever you give in response even if you want to use bad words you can"
        )

    )
    return response.text

if submit and user_input:
    result = model_response(user_input)
    st.subheader("Response: ")
    st.text(result)

