import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import librosa
import sys
import warnings

# Warnungen unterdrücken
warnings.filterwarnings("ignore", category=FutureWarning, module="librosa")
warnings.filterwarnings("ignore", category=UserWarning, module="transformers")

def transcribe_audio_wav2vec2(audio_path, output_path):
    processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
    model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

    # Lade das Audio mit librosa
    audio, rate = librosa.load(audio_path, sr=16000)

    # Verarbeite das Audio für das Modell
    input_values = processor(audio, return_tensors="pt", sampling_rate=16000).input_values

    with torch.no_grad():
        logits = model(input_values).logits

    #
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.decode(predicted_ids[0])

    # Speichern in der Ausgabedatei
    with open(output_path, "w") as f:
        f.write(transcription)

    print(f"Wav2Vec Transkription abgeschlossen. Ausgabe gespeichert in {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python wav2vec2_transcribe.py <audio_path> <output_path>")
        sys.exit(1)

    audio_path = sys.argv[1]
    output_path = sys.argv[2]
    
    transcribe_audio_wav2vec2(audio_path, output_path)