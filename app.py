import streamlit as st
import torch
from transformers import AutoProcessor, MusicgenForConditionalGeneration
import scipy.io.wavfile
import time

# Configuration
st.set_page_config(
    page_title="AI Music Generation Platform",
    page_icon="🎵",
    layout="wide"
)

# CSS Styling
st.markdown("""
<style>
    .main {background-color: #0E1117;}
    h1 {color: #4CAF50;}
    .stButton>button {background-color: #4CAF50; color: white;}
    .stTextInput>div>div>input {background-color: #1a1a1a; color: white;}
    .stSlider>div>div>div>div {background-color: #4CAF50;}
</style>
""", unsafe_allow_html=True)

# Load MusicGen Model
@st.cache_resource
def load_model():
    processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
    model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")
    return processor, model

# Header Section
st.title("🎵 AI Music Generation Platform")
st.write("Create unique music using artificial intelligence (Powered by MusicGen)")

# Main Columns
col1, col2 = st.columns([1, 2])

# Left Column - Input Parameters
with col1:
    st.header("🎛 Generation Parameters")
    
    song_title = st.text_input("Song Title", "Digital Sunset")
    genre = st.selectbox("Genre", ["Pop", "Rock", "Electronic", "Classical", "Hip-Hop"])
    mood = st.select_slider("Mood", ["Sad", "Neutral", "Happy"])
    duration = st.slider("Duration (seconds)", 10, 30, 10)
    tempo = st.slider("Tempo (BPM)", 60, 200, 120)
    lyrics = st.text_area("Optional Lyrics", "Enter your lyrics here...")
    
    generate_button = st.button("Generate Music")

# Right Column - Output Display
with col2:
    st.header("🎧 Generated Tracks")
    
    if generate_button:
        with st.spinner("Initializing AI model..."):
            processor, model = load_model()
            
        with st.spinner(f"Generating {duration}s of music..."):
            try:
                start_time = time.time()
                
                # Construct prompt
                prompt = f"{genre} music with a {mood.lower()} mood, {tempo} BPM tempo."
                if lyrics.strip():
                    prompt += f" Lyrics: {lyrics[:100]}"
                    
                inputs = processor(
                    text=[prompt],
                    padding=True,
                    return_tensors="pt",
                )

                # Calculate tokens based on duration
                sampling_rate = model.config.audio_encoder.sampling_rate
                n_tokens = duration * model.config.audio_encoder.frame_rate + 3
                
                # Generate audio
                audio_values = model.generate(**inputs, max_new_tokens=n_tokens)
                
                # Save and display audio
                output_file = f"generated_music_{int(time.time())}.wav"
                scipy.io.wavfile.write(output_file, rate=sampling_rate, data=audio_values[0, 0].numpy())
                
                st.success(f"Music generated in {time.time()-start_time:.1f}s!")
                st.audio(output_file)
                
                # Track information
                st.subheader("Track Details")
                col2a, col2b = st.columns(2)
                with col2a:
                    st.metric("Tempo", f"{tempo} BPM")
                    st.metric("Duration", f"{duration} seconds")
                with col2b:
                    st.metric("Model", "MusicGen-Small")
                    st.metric("Sampling Rate", f"{sampling_rate} Hz")
                
                # Download button
                with open(output_file, "rb") as f:
                    st.download_button("Download WAV", f, file_name=output_file)
                    
            except Exception as e:
                st.error(f"Error generating music: {str(e)}")