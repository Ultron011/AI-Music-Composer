import streamlit as st
import torchaudio
import os
from audiocraft.models import musicgen
import torch
from datetime import datetime

# Page setup must be first
st.set_page_config(page_title="🎵 AI Music Composer", layout="centered")

# Background animation
st.markdown("""
    <style>
    body {
        background: linear-gradient(270deg, #f3ec78, #af4261, #3c92d1);
        background-size: 600% 600%;
        animation: gradientBG 20s ease infinite;
    }
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .stApp {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 15px;
        padding: 20px;
        margin: 10px;
        backdrop-filter: blur(8px);
    }
    </style>
""", unsafe_allow_html=True)

# Load model
@st.cache_resource
def load_model():
    model = musicgen.MusicGen.get_pretrained('small')
    if torch.cuda.is_available():
        model = model.cuda()
    return model

model = load_model()

# Session state
if "last_audio" not in st.session_state:
    st.session_state.last_audio = None
if "last_prompt" not in st.session_state:
    st.session_state.last_prompt = ""
if "history" not in st.session_state:
    st.session_state.history = []

# Title
st.title("🎶 AI Music Composer")
st.caption("Generate music based on genre, mood, and tempo using Meta’s MusicGen!")

# Input layout in columns
col1, col2 = st.columns(2)
with col1:
    genre = st.text_input("🎼 Genre (e.g. jazz, classical, lo-fi)", value="lo-fi")
    tempo = st.selectbox("⏱ Tempo", ["slow", "mid", "fast"], index=1)
with col2:
    mood = st.selectbox("🎭 Mood", ["happy", "sad", "chill", "energetic", "romantic", "epic"], index=2)
    duration = st.slider("⏳ Duration (seconds)", 5, 30, 10)

# Prompt
prompt = f"A {tempo} tempo {genre} track that feels {mood}"
st.markdown(f"🎙 *Prompt Preview:* {prompt}")

# Generate function
def generate_music():
    model.set_generation_params(duration=duration)
    wav = model.generate([prompt])[0].cpu()

    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.join(output_dir, f"{genre}{mood}{tempo}_{datetime.now().strftime('%Y%m%d%H%M%S')}.wav")
    torchaudio.save(filename, wav, 32000)

    st.session_state.last_audio = filename
    st.session_state.last_prompt = prompt
    st.session_state.history.append(filename)

# Buttons
if st.button("🎧 Generate Music"):
    with st.spinner("🎶 Composing your track..."):
        generate_music()
        st.success("✅ Music generated!")

if st.session_state.last_audio:
    if st.button("🔁 Regenerate"):
        with st.spinner("🎼 Re-composing with same prompt..."):
            generate_music()
            st.success("✅ New version ready!")

# Play audio
if st.session_state.last_audio:
    st.audio(st.session_state.last_audio, format="audio/wav")
    st.download_button("⬇ Download Last Track", open(st.session_state.last_audio, "rb"), file_name=st.session_state.last_audio.split("/")[-1])

# Sidebar: Track history
with st.sidebar:
    st.header("📁 Recent Tracks")
    if st.session_state.history:
        for i, path in enumerate(reversed(st.session_state.history[-5:]), 1):
            st.markdown(f"🎵 Track {i}")
            st.audio(path, format="audio/wav")
            st.download_button(f"⬇ Download Track {i}", open(path, "rb"), file_name=path.split("/")[-1], key=f"dl_{i}")
    else:
        st.info("No tracks generated yet.")