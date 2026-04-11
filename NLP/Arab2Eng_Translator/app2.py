import streamlit as st
from gtts import gTTS
from io import BytesIO
import time
import math

# ------------------------
# Streamlit UI
# ------------------------
st.title("🌍 Arabic Text Voice Reader with Highlighting")
st.write("Type Arabic text below and hear it spoken aloud with word highlighting.")

# Input box
arabic_text = st.text_area("✍️ Enter Arabic text:")

if st.button("Speak Arabic"):
    if arabic_text.strip():
        words = arabic_text.split()
        placeholder = st.empty()  # Placeholder for highlighted text

        chunk_size = 5  # Number of words per audio chunk
        total_chunks = math.ceil(len(words) / chunk_size)

        for i in range(total_chunks):
            start = i * chunk_size
            end = min((i + 1) * chunk_size, len(words))
            chunk_words = words[start:end]

            # ------------------------
            # Highlight current chunk
            # ------------------------
            highlighted_text = ""
            for j, w in enumerate(words):
                if start <= j < end:
                    highlighted_text += f"<span style='background-color: yellow'>{w}</span> "
                else:
                    highlighted_text += w + " "
            placeholder.markdown(highlighted_text, unsafe_allow_html=True)

            # ------------------------
            # Generate TTS for the chunk
            # ------------------------
            tts = gTTS(text=" ".join(chunk_words), lang="ar")
            audio_bytes = BytesIO()
            tts.write_to_fp(audio_bytes)
            audio_bytes.seek(0)
            st.audio(audio_bytes, format="audio/mp3")

            # Delay for smooth playback
            time.sleep(len(chunk_words) * 0.4)  # Adjust speed per word

        st.success("✅ Finished reading!")

    else:
        st.warning("⚠️ Please enter some Arabic text first!")
