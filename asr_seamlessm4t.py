import sys
import os
import seamless_m4t

def transcribe_video_seamlessm4t(video_path, output_path):
    model = seamless_m4t.load_model("base")

    #transcribe video file
    result = model.transcribe(video_path)

    #write transcription to the output file
    with open(output_path, "w") as f:
        f.write(result["text"])

    print(f"Transcription complete. Output saved to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python asr_seamlessm4t.py <video_path> <output_path>")
        sys.exit(1)

    video_path = sys.argv[1]
    output_path = sys.argv[2]

    if not os.path.exists(video_path):
        print(f"Error: The file {video_path} does not exist.")
        sys.exit(1)

    transcribe_video_seamlessm4t(video_path, output_path)