import subprocess
import whisper


# -----------------------------------
# GENERATE SUBTITLES
# -----------------------------------

def generate_srt(audio_file, output_srt):

    print("🧠 Generating subtitles...")

    model = whisper.load_model("base")

    result = model.transcribe(audio_file)

    # -----------------------------------
    # FORMAT TIME
    # -----------------------------------

    def format_time(t):

        hrs = int(t // 3600)
        mins = int((t % 3600) // 60)
        secs = int(t % 60)
        ms = int((t - int(t)) * 1000)

        return (
            f"{hrs:02}:"
            f"{mins:02}:"
            f"{secs:02},"
            f"{ms:03}"
        )

    # -----------------------------------
    # WRITE SRT
    # -----------------------------------

    with open(
        output_srt,
        "w",
        encoding="utf-8"
    ) as f:

        counter = 1

        for segment in result["segments"]:

            raw_text = segment["text"].strip()

            # -----------------------------------
            # SPLIT INTO SMALL CINEMATIC CHUNKS
            # -----------------------------------

            words = raw_text.split()

            chunks = []

            chunk_size = 2

            for i in range(
                0,
                len(words),
                chunk_size
            ):

                chunk = " ".join(
                    words[i:i + chunk_size]
                )

                chunks.append(chunk)

            # -----------------------------------
            # TIMING
            # -----------------------------------

            segment_duration = (
                segment["end"] -
                segment["start"]
            )

            chunk_duration = (
                segment_duration /
                len(chunks)
            )

            # -----------------------------------
            # WRITE EACH CHUNK
            # -----------------------------------

            for j, chunk in enumerate(chunks):

                chunk_start = (
                    segment["start"] +
                    (j * chunk_duration)
                )

                chunk_end = (
                    chunk_start +
                    chunk_duration
                )

                f.write(f"{counter}\n")

                f.write(
                    f"{format_time(chunk_start)} --> "
                    f"{format_time(chunk_end)}\n"
                )

                f.write(f"{chunk}\n\n")

                counter += 1

    print(f"✅ Subtitle created: {output_srt}")


# -----------------------------------
# ADD SUBTITLES TO VIDEO
# -----------------------------------

def add_subtitles(
    video_input,
    subtitle_file,
    output_video
):

    print("🎬 Adding cinematic captions...")

    subtitle_file = subtitle_file.replace(
        "\\",
        "/"
    )

    subtitle_style = (
    "FontName=Georgia,"
    "Fontsize=9,"
    "PrimaryColour=&H00F2F2F2&,"
    "OutlineColour=&H000000&,"
    "BackColour=&H64000000&,"
    "BorderStyle=3,"
    "Outline=1,"
    "Shadow=0,"
    "Alignment=2,"
    "MarginV=35"
)

    cmd = [
        "ffmpeg",
        "-y",
        "-i",
        video_input,

        "-vf",
        (
            "subtitles="
            f"{subtitle_file}:"
            f"force_style='{subtitle_style}'"
        ),

        "-c:a",
        "copy",

        output_video
    ]

    subprocess.run(cmd)

    print(
        f"✅ Final video with captions: "
        f"{output_video}"
    )


# -----------------------------------
# RUN EVERYTHING
# -----------------------------------

if __name__ == "__main__":

    AUDIO_FILE = "audio/full_audio.mp3"

    VIDEO_FILE = "output/final_video.mp4"

    SRT_FILE = "output/subs.srt"

    OUTPUT_VIDEO = (
        "output/final_with_captions.mp4"
    )

    # Generate subtitles
    generate_srt(
        AUDIO_FILE,
        SRT_FILE
    )

    # Burn captions
    add_subtitles(
        VIDEO_FILE,
        SRT_FILE,
        OUTPUT_VIDEO
    )