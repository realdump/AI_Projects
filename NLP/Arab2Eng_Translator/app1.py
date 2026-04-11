import streamlit as st
from gtts import gTTS
from googletrans import Translator

# ------------------------
# Initialize Translator (if needed)
# ------------------------
translator = Translator()

# ------------------------
# Streamlit UI
# ------------------------
st.title("🌍 Arabic Text Voice Reader")
st.write("Type Arabic text below and hear it spoken aloud.")

# Input box
arabic_text = st.text_area("✍️ Enter Arabic text:")

if st.button("Speak Arabic"):
    if arabic_text.strip():
        try:
            # ------------------------
            # Convert Arabic text to speech
            # ------------------------
            tts = gTTS(text=arabic_text, lang="ar")
            tts.save("arabic_output.mp3")

            # Play audio in Streamlit
            with open("arabic_output.mp3", "rb") as audio_file:
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format="audio/mp3")

        except Exception as e:
            st.error(f"Error in reading Arabic text: {e}")

    else:
        st.warning("⚠️ Please enter some Arabic text first!")
