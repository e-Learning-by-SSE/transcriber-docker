import sys
import os
import whisper
import warnings

# Unterdrücke spezifische Warnungen
warnings.filterwarnings("ignore", category=FutureWarning, module="torch")
warnings.filterwarnings("ignore", category=UserWarning, module="whisper")

def transcribe_video_whisper(video_path, output_path):
    model = whisper.load_model("base")

    #transcribe
    result = model.transcribe(video_path)

    #write result to output file
    with open(output_path, "w") as f:
        f.write(result["text"])

    print(f"Transcription complete. Output saved to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python asr_whisper.py <video_path> <output_path>")
        sys.exit(1)

    video_path = sys.argv[1]
    output_path = sys.argv[2]

    if not os.path.exists(video_path):
        print(f"Error: The file {video_path} does not exist.")
        sys.exit(1)

    transcribe_video_whisper(video_path, output_path)