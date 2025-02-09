# 🎵 AI Music Generation Platform

Welcome to the AI Music Generation Platform! This application empowers users to create unique music tracks using artificial intelligence.

**Explore the live application here: [AI Music Generation Platform](https://music-generation-using-ai.streamlit.app/)**

## 🌟 Features

- **AI-Powered Music Creation:** Generate music based on customizable parameters such as genre, mood, tempo, and optional lyrics.
- **Intuitive Interface:** User-friendly controls for setting music generation parameters.
- **Real-Time Playback:** Listen to generated tracks directly within the application.
- **Downloadable Tracks:** Save your creations as WAV files for future enjoyment.

## 🛠️ Pre-Installation Requirements

Before setting up the application, ensure your system meets the following requirements:

- **Operating System:** Windows, macOS, or Linux
- **Python Version:** Python 3.8 or higher
- **Hardware:** A CUDA-enabled GPU is recommended for optimal performance, especially for generating longer music tracks.

## 🚀 Installation

Follow these steps to set up the application:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/ai-music-generation-platform.git
   cd ai-music-generation-platform

	2.	Set Up a Virtual Environment:
It’s recommended to use a virtual environment to manage dependencies.

python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


	3.	Install Dependencies:
Install the required Python packages using pip:

pip install -r requirements.txt


	4.	Configure Environment Variables:
Create a .env file in the project root directory to securely store your API keys:

HUGGINGFACE_API_KEY=your_huggingface_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key

Replace your_huggingface_api_key and your_elevenlabs_api_key with your actual API keys.

🎯 Usage

To run the application:
	1.	Activate the Virtual Environment:

source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


	2.	Start the Streamlit Application:

streamlit run app.py


	3.	Interact with the Application:
	•	Open your web browser and navigate to the URL provided by Streamlit (typically http://localhost:8501).
	•	Use the interface to input your desired parameters:
	•	Song Title: Name your track.
	•	Genre: Select from options like Pop, Rock, Electronic, Classical, or Hip-Hop.
	•	Mood: Choose the mood of the music (Sad, Neutral, Happy).
	•	Duration: Set the length of the track in seconds.
	•	Tempo: Adjust the beats per minute (BPM).
	•	Optional Lyrics: Provide lyrics to influence the music generation.
	•	Click the “Generate Music” button to create your track. The generated music will be displayed on the right side of the interface, where you can listen to it and download the WAV file.

🖥️ System Requirements
	•	Hardware: A CUDA-enabled GPU is recommended for optimal performance. Generating music without a GPU may be significantly slower and is not recommended for longer durations.
	•	Memory: At least 8GB of RAM is recommended.
	•	Storage: Ensure you have sufficient disk space (~5GB) for model files and generated outputs.

🙏 Acknowledgements

This application utilizes the following open-source projects:
	•	MusicGen by Meta
	•	Hugging Face Transformers
	•	Streamlit
