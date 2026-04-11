import streamlit as st
from gtts import gTTS
from googletrans import Translator

# ------------------------
# Initialize Translator
# ------------------------
translator = Translator()

# ------------------------
# Streamlit UI
# ------------------------
st.title("🌍 Arabic → English Voice Translator (Google Translate)")
st.write("Type Arabic text below and get an English translation with voice output.")

# Input box
arabic_text = st.text_area("✍️ Enter Arabic text:")

if st.button("Translate & Speak"):
    if arabic_text.strip():
        try:
            # ------------------------
            # Translate using Google Translate
            # ------------------------
            translation = translator.translate(arabic_text, src='ar', dest='en')
            english_text = translation.text

            # Show translation
            st.subheader("✅ English Translation:")
            st.success(english_text)

            # ------------------------
            # Convert to Speech
            # ------------------------
            tts = gTTS(text=english_text, lang="en")
            tts.save("output.mp3")

            # Play audio in Streamlit
            with open("output.mp3", "rb") as audio_file:
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format="audio/mp3")

        except Exception as e:
            st.error(f"Error in translation: {e}")

    else:
        st.warning("⚠️ Please enter some Arabic text first!")
