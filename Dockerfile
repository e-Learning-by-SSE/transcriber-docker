
# Verwende das Python 3.9-slim Image als Basis
FROM python:3.9-slim

# Erstelle das Arbeitsverzeichnis im Container
WORKDIR /usr/src/app

# Installiere Systemabhängigkeiten
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    && rm -rf /var/lib/apt/lists/*

# Installiere Python-Abhängigkeiten
RUN pip install --no-cache-dir openai-whisper jiwer torch torchvision torchaudio transformers librosa

# Kopiere die Python- und Bash-Skripte in den Container
COPY . .

# Mache das Bash-Skript ausführbar
RUN chmod +x run_asr.sh

# Definiere den Entry Point für das Bash-Skript
ENTRYPOINT ["./run_asr.sh"]
