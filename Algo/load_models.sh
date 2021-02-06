MODEL_DIRS=$PWD/models

mkdir $MODEL_DIRS
cd $MODEL_DIRS

wget https://alphacephei.com/vosk/models/vosk-model-en-us-aspire-0.2.zip -O $MODEL_DIRS/model-en.zip
unzip $MODEL_DIRS/model-en.zip -d $MODEL_DIRS
#rm -f $MODEL_DIRS/model-en.zip

wget https://alphacephei.com/vosk/models/vosk-model-ru-0.10.zip -O $MODEL_DIRS/model-ru.zip
unzip $MODEL_DIRS/model-ru.zip -d $MODEL_DIRS
#rm -f $MODEL_DIRS/model-ru.zip