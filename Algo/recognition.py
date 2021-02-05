#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer, SetLogLevel
import sys
import os
import json
import subprocess

MODELS_DIR = 'models'
MODELS = {
    'ru': 'vosk-model-ru-0.10'
}

def get_audio_stream(path, sample_rate=16000):
    if not os.path.exists(path):
        raise Exception('Invalid path')

    process = subprocess.Popen(['ffmpeg', '-loglevel', 'quiet', '-i',
                            str(path),
                            '-ar', str(sample_rate) , '-ac', '1', '-f', 's16le', '-'],
                            stdout=subprocess.PIPE)
    return process

def recongitize_vosk(path, model='ru', sample_rate=16000):
    if model not in MODELS:
        raise Exception('Invalid model')

    stream = get_audio_stream(path, sample_rate)
    print(os.path.join(MODELS_DIR, MODELS[model]))
    model = Model(os.path.join(MODELS_DIR, MODELS[model]))
    rec = KaldiRecognizer(model, sample_rate)

    while True:
        data = stream.stdout.read(4000)
        if len(data) == 0:
            break
        rec.AcceptWaveform(data)

    result = json.loads(rec.FinalResult())

    return result['text']
    


if __name__ == '__main__':
    SetLogLevel(0)

    result = recongitize_vosk(sys.argv[0])
    print(result)
