from tools.video_generator import create_single_image_video


def run_video_agent(image_path, audio_path):
    print("🎬 Creating final video...")

    create_single_image_video(
        image_path=image_path,
        audio_path=audio_path,
        output="output/final_video.mp4"
    )

    print("✅ Final video created")