
#! pip3 install pyaudio
#! pip3 install vosk
from vosk import Model, KaldiRecognizer
import os
import pyaudio
import json


MODEL_PATH="/mnt/boveda/VOSK/vosk-model-es-0.42";

# Validacao da pasta de modelo
# Eh necessario criar a pasta model-br a partir de onde estiver este fonte
if not os.path.exists(MODEL_PATH):
    print ("Modelo em portugues nao encontrado.")
    exit (1)

# Preparando o microfone para captura
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

# Apontando o algoritmo para ler o m odelo treinado na pasta MODEL_PATH
model = Model(MODEL_PATH)
rec = KaldiRecognizer(model, 16000)

# Criando um loop continuo para ficar ouvindo o microfone
while True:
    # Lendo audio do microfone
    data = stream.read(4000)
    
    # Convertendo audio em texto
    if rec.AcceptWaveform(data):
        cad=rec.Result();
        obj_dict = json.loads(cad);
        texto=obj_dict["text"];
        
        print("<<",texto)
        
        if(texto.lower()=='lautaro'):
            resposta='Mande?';
            print(">>",resposta)
        
        
