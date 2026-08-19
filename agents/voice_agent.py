from tools.voice_generator import generate_voice
from tools.merge_audio import merge_audio

def run_voice_agent():
    with open("memory/script.txt", "r", encoding="utf-8") as f:
        script = f.read()

    print("🎙 Generating voice...")

    audio_files = generate_voice(script)

    print("🔗 Merging audio...")

    output_audio = merge_audio(audio_files, "audio/full_audio.mp3")

    print("✅ Full audio created:", output_audio)

    return output_audio   # ✅ VERY IMPORTANT