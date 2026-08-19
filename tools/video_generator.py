import os
import subprocess
# ✅ Ensure ffmpeg is found
os.environ["IMAGEIO_FFMPEG_EXE"] = "C:/ffmpeg-8.1-essentials_build/bin/ffmpeg.exe"

#from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
from moviepy.editor import (
    ImageClip,
    AudioFileClip,
    CompositeAudioClip,
    concatenate_videoclips
)
from PIL import Image

# 👉 Path to your generated images
OUTPUT_FOLDER = "C:/Users/deepa/imageai/ComfyUI/output"


# 🔥 FIX: Convert PNG → proper RGB JPG
def prepare_image(input_path, output_path):
    try:
        img = Image.open(input_path).convert("RGB")  # KEY FIX
        img.save(output_path, "JPEG")
        print(f"✅ Converted: {input_path} → {output_path}")
    except Exception as e:
        print(f"❌ Error converting image: {e}")


def create_single_image_video(image_path, audio_path, output="final_video.mp4"):
    print("🎬 Creating video from single image...")

    # 🔥 Delete old video if exists (prevents permission errors)
    if os.path.exists(output):
        try:
            os.remove(output)
        except:
            print("⚠️ Could not delete old video. Close video player if open.")
            return

    # 🔥 FFmpeg command
    cmd = [
        "ffmpeg",
        "-y",                      # overwrite
        "-loop", "1",              # loop image
        "-i", image_path,          # image
        "-i", audio_path,          # audio
        "-c:v", "libx264",
        "-tune", "stillimage",
        "-c:a", "aac",
        "-b:a", "192k",
        "-pix_fmt", "yuv420p",
        "-shortest",               # stop when audio ends
        output
    ]

    subprocess.run(cmd)

    print(f"✅ Video created: {output}")

def create_video(images, audio_files):
    clips = []

    temp_folder = "temp_images"
    os.makedirs(temp_folder, exist_ok=True)

    for i, (img, audio) in enumerate(zip(images, audio_files)):

        img_path = os.path.join(OUTPUT_FOLDER, img)
        temp_img = os.path.join(temp_folder, f"img_{i}.jpg")

        print(f"Processing: {img_path} + {audio}")

        if not os.path.exists(img_path):
            print(f"❌ Image not found: {img_path}")
            continue

        if not os.path.exists(audio):
            print(f"❌ Audio not found: {audio}")
            continue

        # 🔥 Convert image properly
        prepare_image(img_path, temp_img)

        if not os.path.exists(temp_img):
            print(f"❌ Temp image not created: {temp_img}")
            continue

        try:
            #audio_clip = AudioFileClip(audio)

            #clip = (
            #   ImageClip(temp_img)
            #    .set_duration(audio_clip.duration)
            #   .set_audio(audio_clip)
            #   .resize((720, 1280))  # 📱 vertical format for shorts
            #)

            #clips.append(clip)
            # -----------------------------------
            # MAIN NARRATION
            # -----------------------------------

            voice_audio = AudioFileClip(audio)

            # -----------------------------------
            # BACKGROUND PIANO
            # -----------------------------------

            bg_music = (
                AudioFileClip("assets/emotional_piano.mp3")
                .volumex(0.18)   # soft volume
            )

            # match narration length
            bg_music = bg_music.subclip(
                0,
                voice_audio.duration
            )

            # -----------------------------------
            # OPTIONAL RAIN AMBIENCE
            # -----------------------------------

            rain_audio = (
                AudioFileClip("assets/rain.mp3")
                .volumex(0.05)
            )

            rain_audio = rain_audio.subclip(
                0,
                voice_audio.duration
            )

            # -----------------------------------
            # COMBINE AUDIO
            # -----------------------------------

            final_audio = CompositeAudioClip([
                rain_audio,
                bg_music,
                voice_audio
            ])

            # -----------------------------------
            # CREATE VIDEO CLIP
            # -----------------------------------

            clip = (
                ImageClip(temp_img)
                .set_duration(voice_audio.duration)
                .set_audio(final_audio)
                .resize((720, 1280))
            )
            clips.append(clip)

        except Exception as e:
            print(f"❌ Error creating clip: {e}")

    if not clips:
        print("❌ No clips created")
        return

    print("🎬 Combining clips...")

    final = concatenate_videoclips(clips, method="compose")

    print("🚀 Writing final video...")

    final.write_videofile(
        "final_video.mp4",
        fps=24,
        codec="libx264",
        audio_codec="aac"
    )

    print("✅ Final video created: final_video.mp4")