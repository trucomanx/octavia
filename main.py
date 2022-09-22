#!/usr/bin/python

#!pip3 install pyaudio
#!pip3 install vosk

import sys 
sys.path.append('library')

################################################################################

from vosk import Model, KaldiRecognizer
import os
import pyaudio
import json



################################################################################
## VARIABLES 

filename_tmp="temporal-file-trash.mp3" # temporal file
language = 'es'; # Language in which you want to convert
MODEL_PATH="/mnt/boveda/VOSK/vosk-model-es-0.42";

####################################################

def command_open_program(program):
    os.system( program)
# user define function
def command_shutdown():
    return os.system("shutdown -P")
 
def command_restart():
    return os.system("shutdown -r")

'''
def command_logout():
    return os.system("shutdown -l")
'''

import speaklib

####################################################


# Preparando o microfone para captura
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

# Apontando o algoritmo para ler o m odelo treinado na pasta MODEL_PATH
if not os.path.exists(MODEL_PATH):
    print ("Modelo em portugues nao encontrado.")
    exit (1)
model = Model(MODEL_PATH)
rec = KaldiRecognizer(model, 16000)



enable_command=False;

# Criando um loop continuo para ficar ouvindo o microfone
while True:
    # Lendo audio do microfone
    data = stream.read(4000)
    
    
    if rec.AcceptWaveform(data):
        cad=rec.Result();
        obj_dict = json.loads(cad);
        texto=obj_dict["text"].lower();
        
        if len(texto)>0:
            print("<<",texto)
            
            if (texto=='octavia'):
                resposta='Sí, en qué puedo ayudar?';
                speaklib.speak_the_text(stream,resposta,lang=language,ftemp=filename_tmp);
                print(">>",resposta)
                
                enable_command=True;
            elif enable_command==True:
            
                if (texto=='desconecta la computadora'):
                    command_shutdown();
                    
                    resposta='desconectando la computadora, por favor espere ...';
                    speaklib.speak_the_text(stream,resposta,lang=language,ftemp=filename_tmp);
                    print(">>",resposta)
                    enable_command=False;
                else:
                    command_open_program(texto);
                    
                    resposta='Abriendo: '+texto;
                    speaklib.speak_the_text(stream,resposta,lang=language,ftemp=filename_tmp);
                    print(">>",resposta)
                    enable_command=False;
        
