#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer, SetLogLevel
import sys
import os
import json
import subprocess
#from punctuator import Punctuator

MODELS_DIR = 'models'
MODELS = {
    'ru': 'vosk-model-ru-0.10',
    'en': 'vosk-model-en-us-aspire-0.2'
}
PUNCTUATOR_MODEL = ''
SetLogLevel(-1)

def get_audio_stream(path, sample_rate=16000):
    if not os.path.exists(path):
        raise Exception('Invalid path')

    process = subprocess.Popen(['ffmpeg', '-loglevel', 'quiet', '-i',
                            str(path),
                            '-ar', str(sample_rate) , '-ac', '1', '-f', 's16le', '-'],
                            stdout=subprocess.PIPE)
    return process

def recongitize_vosk(path, model='ru', sample_rate=16000, progress_callback=None):
    if model not in MODELS:
        raise Exception('Invalid model')

    stream = get_audio_stream(path, sample_rate)
    model = Model(os.path.join(MODELS_DIR, MODELS[model]))
    rec = KaldiRecognizer(model, sample_rate)
    it = 0
    while True:
        data = stream.stdout.read(4000)
        if len(data) == 0:
            break
        it += 1
        rec.AcceptWaveform(data)
    
    raw = json.loads(rec.FinalResult())
    
    return raw

def text_processing_ru(path, progress_callback=None):
    raw = recongitize_vosk(path, "ru", progress_callback=progress_callback)

    # TODO: Language processing
    
    result = raw['text']

    return result

def text_processing_en(path, progress_callback=None):
    raw = recongitize_vosk(path, "en", progress_callback=progress_callback)

    # TODO: Language processing

    #p = Punctuator(PUNCTUATOR_MODEL)
    #result = p.punctuate(raw['text'])
    
    result = raw['text']

    return result    


def text_processing(path, lang="ru", progress_callback=None):
    if lang == "ru":
        return text_processing_ru(path, progress_callback=progress_callback)
    elif lang == "en":
        return text_processing_en(path, progress_callback=progress_callback)
    else:
        raise Error("Invalid language")


if __name__ == '__main__':
    SetLogLevel(0)

    result = text_processing(sys.argv[1], sys.argv[2] if len(sys.argv) >= 2 else "ru")
    print(result)
