
# transcribr

Ein Projekt für die automatische Transkription von Videos und Evaluierung der verwendeten ASR Tools.


## Voraussetzungen

#### Docker installieren

Das Projekt läuft in einem Docker-Container, der alle benötigten Abhängigkeiten und Modelle enthält. Installiere Docker, falls es noch nicht vorhanden ist.

Für Windows und macOS: Lade Docker Desktop herunter und installiere es. Starte Docker Desktop.

## Installation

### 1. Repository klonen

```bash
git clone https://github.com/e-Learning-by-SSE/transcriber-docker.git
cd transcriber-docker 
```

### 2. Docker-Image erstellen

```bash
docker build -t asr_container .
```
    
### 3. Verzeichnisstruktur einrichten
Die folgenden Verzeichnisse müssen vorhanden sein:
- `input_videos`: Enthält die Videos, die transkribiert werden sollen.
- `ground_truth`: Enthält die Ground-Truth-Textdateien für die Transkriptionen.
- `output`: Die Ausgaben werden hier abgelegt.

## Ausführen

### 1. Videos ablegen
Lege die Videodateien (.mp4, .mkv, .avi) in den Ordner input_videos.

### 2. Ground-Truth-Dateien hinzufügen
Stelle sicher, dass für jede Videodatei eine entsprechende Ground-Truth-Textdatei im Ordner ground_truth vorliegt. Der Name der Datei muss mit dem Namen des Videos übereinstimmen (z.B., Hochwasser.mp4 und Hochwasser.txt).

### 3. Docker-Container starten
Führe das Projekt im Docker-Container aus und übergebe die Verzeichnispfade:

```bash
docker run --rm     -v $(pwd)/input_videos:/usr/src/app/input_videos     -v $(pwd)/output:/usr/src/app/output     -v $(pwd)/ground_truth:/usr/src/app/ground_truth     asr_container /usr/src/app/input_videos /usr/src/app/output /usr/src/app/ground_truth
```

