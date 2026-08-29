# 🎬 AI Content Creation Agent

An end-to-end AI content creation pipeline that automatically generates YouTube Shorts and Instagram Reels from a single topic.

The project uses local AI models to generate scripts, images, voiceovers, subtitles, and videos.

---

# 🚀 Features

- 📝 AI Script Generation (Ollama + Llama3)
- 🖼️ AI Image Generation (ComfyUI + Stable Diffusion)
- 🎙️ AI Voice Generation (Edge TTS)
- 🎥 Automatic Video Creation (MoviePy)
- 💬 Automatic Subtitle Generation (Whisper)
- 🎞️ Subtitle Rendering (FFmpeg)
- 📱 Ready for YouTube Shorts & Instagram Reels

---

# 🏗 Project Architecture

```

                 User Topic
                      │
                      ▼
               main_agent.py
                      │
     ┌────────────────┼─────────────────┐
     ▼                ▼                 ▼
Script Agent     Image Agent      Voice Agent
     │                │                 │
     ▼                ▼                 ▼
 Ollama          ComfyUI           Edge-TTS
     │                │                 │
     └──────────┬─────┴─────────────────┘
                ▼
          Video Agent
                │
            MoviePy
                │
                ▼
       Captions Agent
                │
            Whisper
                │
                ▼
             FFmpeg
                │
                ▼
          Final Reel.mp4

```

---

# 📂 Project Structure

```

contentCreationAgent/

│

├── agents/
│ ├── script_agent.py
│ ├── image_agent.py
│ ├── voice_agent.py
│ ├── video_agent.py
│ └── captions_agent.py

│

├── tools/
│ ├── generator.py
│ ├── image_generator.py
│ ├── video_generator.py
│ ├── add_captions.py
│ └── ...

│

├── memory/
│ ├── script.txt
│ ├── title.txt
│ ├── hashtags.txt
│ └── ...

│

├── output/

│

├── main_agent.py

│

├── requirements.txt

│

└── README.md

```

---

# ⚙ Requirements

- Python 3.10
- Ollama
- Llama3 Model
- ComfyUI
- Stable Diffusion Model
- FFmpeg

---

# 📦 Python Packages

```bash
pip install -r requirements.txt
```

or

```bash
pip install \
requests \
moviepy==1.0.3 \
python-dotenv \
edge-tts \
opencv-python \
openai-whisper \
pillow \
pysrt
```

---

# 🧠 Install Ollama

Download:

https://ollama.com

Install Llama3

```bash
ollama pull llama3
```

Check installation

```bash
ollama list
```

---

# 🎨 Install ComfyUI

Install ComfyUI.

Place your Stable Diffusion model inside

```

ComfyUI/models/checkpoints/

```

Start ComfyUI

```bash
python main.py
```

The server should run on

```

http://127.0.0.1:8188

```

---

# 🎬 Install FFmpeg

Install FFmpeg and add it to PATH.

Verify

```bash
ffmpeg -version
```

---

# 🚀 Running the Project

Start Ollama

```bash
ollama serve
```

If already running, skip this step.

---

Start ComfyUI

```bash
python main.py
```

---

Activate virtual environment

```bash
cd contentCreationAgent

.\venv\Scripts\activate
```

---

Run the project

```bash
python main_agent.py
```

Enter a topic

```

self love

```

---

# 📂 Output

The project generates

```

script.txt

title.txt

hashtags.txt

image.png

voice.mp3

video.mp4

subtitles.srt

final_video.mp4

```

---

# 🧩 Technologies Used

| Tool | Purpose |
|-------|----------|
| Ollama | AI Script Generation |
| Llama3 | Language Model |
| ComfyUI | AI Image Generation |
| Stable Diffusion | Image Model |
| Edge TTS | Voice Generation |
| MoviePy | Video Editing |
| Whisper | Subtitle Generation |
| FFmpeg | Video Rendering |

---

# 📈 Future Improvements

- Google ADK Integration
- Multi-agent workflow
- Automatic YouTube Upload
- Automatic Instagram Upload
- AI Thumbnail Generation
- AI Music Generation
- Scheduler
- Multiple Languages
- Gemini Support
- Flux Support

---

# 👨‍💻 Author

Deepa

AI Automation • Content Creation • Multi-Agent Systems
