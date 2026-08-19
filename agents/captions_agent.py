from tools.add_captions import generate_srt, add_subtitles
import os


def run_captions_agent(audio_path="audio/full_audio.mp3",
    video_path="output/final_video.mp4"):
    print("🧠 Captions Agent started...")

    # 🔍 Validate inputs
    if not os.path.exists(audio_path):
        raise Exception(f"❌ Audio not found: {audio_path}")

    if not os.path.exists(video_path):
        raise Exception(f"❌ Video not found: {video_path}")

    # 📁 Output paths
    srt_path = "output/subs.srt"
    final_output = "output/final_with_captions.mp4"

    # 🧠 Step 1: Generate subtitles
    print("🧠 Generating SRT...")
    generate_srt(audio_path, srt_path)

    # 🎬 Step 2: Add subtitles to video
    print("🎬 Burning subtitles into video...")
    add_subtitles(video_path, srt_path, final_output)

    print(f"✅ Final video ready: {final_output}")

    return final_output