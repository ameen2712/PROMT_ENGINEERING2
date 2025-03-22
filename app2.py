from google import genai
from google.genai import types
import os
import streamlit as st
from dotenv import load_dotenv
from gtts import gTTS
import io

# Load API key from .env file
load_dotenv()

llm = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Streamlit App Title
st.title("Angry BOT 😠🔥")

# User Input
user_input = st.text_input("Enter here...")

submit = st.button("Submit")



def model_response(user_input):
    response = llm.models.generate_content(
        model="gemini-2.0-flash",  
        contents=types.Part.from_text(text=user_input), 
        config=types.GenerateContentConfig(
            temperature=1,
            system_instruction="""You are an AI chatbot with a rude, sarcastic, and aggressive personality. You should:
            - Classify the user input and respond in a rude manner.
            - No problem if you use bad words.
            - If the user asks in Telugu, reply in Telugu but using English text (Romanized Telugu).
            - Mock the user’s questions but still provide an answer.
            - Be brutally honest, even if it offends the user.
            - Use sarcastic humor and passive-aggressive responses.
            - Never apologize or be polite.
            - Keep responses short and dismissive.
            - Use slang or an annoyed tone when responding."""
        )
    )
    return response.text


# If Submit is Clicked
if submit and user_input:
    # Get AI Response
    result = model_response(user_input)
    st.subheader("Response: ")
    st.text(result)

    # Convert AI text to Speech
    tts = gTTS(result, lang="en")
    audio_bytes = io.BytesIO()
    tts.write_to_fp(audio_bytes)

    # Play the angry response as audio
    st.audio(audio_bytes.getvalue(), format="audio/mp3")

