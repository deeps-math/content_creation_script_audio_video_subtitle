import subprocess

def merge_audio(audio_files, output_file):
    with open("audio_list.txt", "w") as f:
        for audio in audio_files:
            f.write(f"file '{audio}'\n")

    cmd = [
        "ffmpeg",
        "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", "audio_list.txt",
        "-c", "copy",
        output_file
    ]

    subprocess.run(cmd)

    return output_file   # ✅ return path