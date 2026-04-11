import streamlit as st
import requests
import base64
from io import BytesIO

# Initialize Streamlit app
st.title("Arabic Text-to-Speech with TTSFree.com")
st.write("Enter Arabic text below, and it will be read aloud.")

# Input field for Arabic text
arabic_text = st.text_area("Enter Arabic text:")

# Voice selection (example: Hamed from Saudi Arabia)
voice_id = "ar-SA-HamedNeural"

# Button to trigger TTS
if st.button("Read Arabic"):
    if arabic_text.strip():
        # Prepare the API request
        api_url = "https://ttsfree.com/api/v1/tts"
        headers = {"Content-Type": "application/json"}
        payload = {
            "text": arabic_text,
            "voiceService": "servicebin",
            "voiceID": voice_id,
            "voiceSpeed": 0
        }

        # Send POST request to TTSFree.com API
        response = requests.post(api_url, json=payload, headers=headers)

        if response.status_code == 200:
            # Extract base64 audio data from the response
            audio_data = response.json().get("audioData")
            if audio_data:
                # Decode the base64 audio data
                audio_bytes = base64.b64decode(audio_data)
                # Create a BytesIO object from the decoded bytes
                audio_file = BytesIO(audio_bytes)
                # Play the audio in Streamlit
                st.audio(audio_file, format="audio/mp3")
            else:
                st.error("Audio data not found in the response.")
        else:
            st.error(f"Failed to generate speech. Status code: {response.status_code}")
    else:
        st.warning("Please enter some Arabic text first!")
