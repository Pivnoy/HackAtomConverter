mkdir models
cd models

wget https://alphacephei.com/vosk/models/vosk-model-en-us-aspire-0.2.zip
unzip vosk-model-en-us-aspire-0.2.zip
rm -f vosk-model-en-us-aspire-0.2.zip

wget https://alphacephei.com/vosk/models/vosk-model-ru-0.10.zip
unzip vosk-model-ru-0.10.zip
rm -f vosk-model-ru-0.10.zip
