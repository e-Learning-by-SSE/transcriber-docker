#!/bin/bash

#ASR bash script für Whisper und andere ASR Tools
#Benutzung: ./run_asr.sh <video_directory> <output_directory> <ground_truth_directory>

# Anzahl der übergebenen Argumente überprüfen
if [ "$#" -ne 3 ]; then
  echo "Usage: $0 <video_directory> <output_directory> <ground_truth_directory>"
  exit 1
fi

# Variablen zuweisen 
VIDEO_DIR="$1"
OUTPUT_DIR="$2"
GROUND_TRUTH_DIR="$3"

# prüfe ob das Videoverzeichnis existiert
if [ ! -d "$VIDEO_DIR" ]; then
  echo "error: The provided video directory does not exist."
  exit 1
fi

# prüfe ob die Ausgabeordner existieren oder erstelle die
mkdir -p "$OUTPUT_DIR/whisper"
#mkdir -p "$OUTPUT_DIR/seamlessm4t"
mkdir -p "$OUTPUT_DIR/Wav2Vec"
mkdir -p "$OUTPUT_DIR/wer_comparisons"

# prüfe ob das GroundTruth Verzeichnis existiert
if [ ! -d "$GROUND_TRUTH_DIR" ]; then
  echo "error: THe provided ground truth directory does not exist."
  exit 1
fi

# iteriere durch jedes Video in dem Verzeichnis
for video_file in "$VIDEO_DIR"/*; do
  if [[ $video_file == *.mp4 || $video_file == *.mkv || $video_file == *.avi ]]; then
    # Video Dateiname ohne Endung
    filename=$(basename -- "$video_file")
    filename_without_ext="${filename%.*}"

    # Pfad zu der Transkribierung
    whisper_output="$OUTPUT_DIR/whisper/$filename_without_ext.txt"
    #seamlessm4t_output="$OUTPUT_DIR/seamlessm4t/$filename_without_ext.txt"
    wav2vec_output="$OUTPUT_DIR/wav2vec/$filename_without_ext.txt"
    
    # Ground truth 
    ground_truth_file="$GROUND_TRUTH_DIR/$filename_without_ext.txt"
    
    # prüfe ob die GroundTruth existiert
    if [ ! -f "$ground_truth_file" ]; then
      echo "Warning: No ground truth found for $filename, skipping WER comparison."
      continue
    fi

    #Whisper ASR
    echo "Processing $video_file with Whisper..."
    python3 asr_whisper.py "$video_file" "$whisper_output"
    
    # Wav2Vec 2.0-Transkription
    echo "Processing $video_file with Wav2Vec 2.0-Transkription..."
    python3 wav2vec2_transcribe.py "$video_file" "$wav2vec_output"
    
    # Run SeamlessM4T ASR
    #echo "Processing $video_file with SeamlessM4T..."
    #python3 asr_seamlessm4t.py "$video_file" "$seamlessm4t_output"
    
    # prüfe ob die output Datei erstellt wurde
    if [ -f "$whisper_output" ] && [ -f "$wav2vec_output" ]; then
      # vergleiche WER für den Output mit der Ground Truth
      comparison_output="$OUTPUT_DIR/wer_comparisons/$filename_without_ext.txt"
      echo "Comparing WER for $filename..."
      python3 wer_comparison.py "$ground_truth_file" "$whisper_output" "$wav2vec_output" "$comparison_output"
    else
      echo "Error: Transcription failed for $video_file."
    fi
  fi
done