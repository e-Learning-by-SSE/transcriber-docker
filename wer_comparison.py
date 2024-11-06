import sys
import jiwer

def calculate_wer(reference, hypothesis):
    """Calculate WER between reference and hypothesis."""
    return jiwer.wer(reference, hypothesis)

def load_text(file_path):
    """Load text from file."""
    with open(file_path, "r") as f:
        return f.read().strip()
    
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python wer_comparison.py <ground_truth_file> <whisper_output> <wav2vec_output> <comparison_output>")
        sys.exit(1)

    ground_truth_file = sys.argv[1]
    whisper_output = sys.argv[2]
    wav2vec_output = sys.argv[3]
    comparison_output = sys.argv[4]

    #ground truth und transcriptions laden
    ground_truth = load_text(ground_truth_file)
    whisper_transcription = load_text(whisper_output)
    wav2vec_transcription = load_text(wav2vec_output)

    video_name = ground_truth_file.split("/")[-1].split(".")[0]

    #berechne WER 
    whisper_wer = calculate_wer(ground_truth, whisper_transcription)
    wav2vec_wer = calculate_wer(ground_truth, wav2vec_transcription)

    try:
        with open(comparison_output, "r") as f:
            pass
    except FileNotFoundError:
        with open(comparison_output, "w") as f:
            f.write("ASR Modell, Video, WER\n") 

    # Append the WER results to the file
    with open(comparison_output, "a") as f:  
        f.write(f"Whisper, {video_name}, {whisper_wer}\n")
        f.write(f"Wav2Vec, {video_name}, {wav2vec_wer}\n")

    print(f"WER comparison for {video_name} saved to {comparison_output}")