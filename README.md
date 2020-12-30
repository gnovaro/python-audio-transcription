# Python audio transcription

```terminal
sudo apt-get install -y build-essential swig libpulse-dev python3-pocketsphinx
sudo apt-get install -y pocketsphinx
```

```terminal
pip3 install pydub SpeechRecognition
```

## Make sure we have up-to-date versions of pip, setuptools and wheel:
```terminal
pip3 install --upgrade pip setuptools wheel

pip3 install --upgrade pocketsphinx
```

## Example:
Convert first video to mp3
```terminal
ffmpeg -i video.mp4 -f mp3 audio.mp3
```

Run python app
```terminal
python3 main.py audio.mp3
```