import streamlit as st
import pyttsx3
import time

# ------------------------
# Initialize pyttsx3
# ------------------------
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Select male voice (usually voice[0] is male)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)  # Speech rate

# ------------------------
# Streamlit UI
# ------------------------
st.set_page_config(page_title="Arabic Text Reader", layout="wide")
st.title("🌍 Arabic Text Reader with Male Voice & Highlighting")
st.write("Type Arabic text below, it will be read aloud word by word.")

# ------------------------
# Session state to keep text across reruns
# ------------------------
if 'arabic_text' not in st.session_state:
    st.session_state['arabic_text'] = ''

# Dynamic height based on number of lines
num_lines = max(5, st.session_state['arabic_text'].count('\n') + 1)
text_input = st.text_area(
    "Enter Arabic text:",
    value=st.session_state['arabic_text'],
    height=num_lines * 40  # 40px per line
)
st.session_state['arabic_text'] = text_input

# ------------------------
# Read Arabic Button
# ------------------------
if st.button("Read Arabic"):
    if st.session_state['arabic_text'].strip():
        words = st.session_state['arabic_text'].split()
        highlighted_text = st.session_state['arabic_text']

        placeholder = st.empty()  # Placeholder for highlighted text

        for word in words:
            # Highlight current word
            highlighted_text = highlighted_text.replace(
                word, f"<span style='background-color: yellow'>{word}</span>", 1
            )
            placeholder.markdown(highlighted_text, unsafe_allow_html=True)

            # Speak the word
            engine.say(word)
            engine.runAndWait()

            time.sleep(0.05)  # small delay for readability

        st.success("✅ Finished reading!")
    else:
        st.warning("⚠️ Please enter some Arabic text first!")
