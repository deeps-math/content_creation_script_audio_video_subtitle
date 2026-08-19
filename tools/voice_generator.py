import asyncio
import edge_tts
import os

VOICE = "en-US-JennyNeural"


async def generate_line(text, file_path):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(file_path)


def generate_voice(script):
    lines = [l.strip() for l in script.split("\n") if l.strip()]

    os.makedirs("audio", exist_ok=True)
    audio_files = []

    for i, line in enumerate(lines):
        file_path = f"audio/line_{i}.mp3"
        print(f"🎙 Generating voice {i+1}...")

        asyncio.run(generate_line(line, file_path))
        audio_files.append(file_path)

    return audio_files