import os
import subprocess
from agents.script_agent import run_script_agent
from agents.image_agent import run_image_agent
from agents.voice_agent import run_voice_agent
from agents.video_agent import run_video_agent
from agents.captions_agent import run_captions_agent


def file_exists(path):
    return os.path.exists(path) and os.path.getsize(path) > 0

def clean_old_files():
    print("🧹 Cleaning old files...")

    folders = ["audio", "output", "temp_images"]
    files = ["script.txt", "title.txt", "hashtags.txt", "audio/full_audio.mp3", "final_video.mp4"]

    # remove files
    for f in files:
        if os.path.exists(f):
            try:
                os.remove(f)
            except:
                print(f"⚠️ Could not delete {f} (maybe open)")

    # remove temp videos
    for i in range(20):
        temp_file = f"temp_{i}.mp4"
        if os.path.exists(temp_file):
            try:
                os.remove(temp_file)
            except:
                pass

    print("✅ Cleanup done\n")




if __name__ == "__main__":
    topic = input("Enter topic: ")
       # 🔥 Always start fresh
    print("cleaning old files...")
    clean_old_files()
    print("🧠 Script  → generating...")
    script=run_script_agent(topic)
   
    print("🎨 Image  → generating...")
    image_path = run_image_agent(topic)
    print("🎙 Audio  → generating...")
    audio_path = run_voice_agent()
    print("🎬 Creating final video...")
    print("🎬 Creating final video...")
    run_video_agent(image_path, audio_path)

    print("🧠 Generating subtitles...")
    print("🎬 Creating final video...")
    video_path = run_video_agent(image_path, audio_path)

    print("🧠 Running captions agent...")
    final_video = run_captions_agent(
    audio_path="audio/full_audio.mp3",
    video_path="output/final_video.mp4"
    )

    print("\n🚀 DONE! Check output/final_with_captions.mp4")