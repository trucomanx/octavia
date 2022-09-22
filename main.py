#!/usr/bin/python

#!pip3 install pyaudio
#!pip3 install vosk
#!pip3 install json
#!pip3 install webbrowser

import sys 
sys.path.append('library')

################################################################################

# externas
from vosk import Model, KaldiRecognizer
import pyaudio
import json
import os

# propia
import speaklib
import processinglib


################################################################################
## VARIABLES 

'''
language = 'es';
vosk_model_path="/mnt/boveda/VOSK/vosk-model-es-0.42";
response_text='Sí, en qué puedo ayudar?';
octavia_name='octavia';
initial_msg='octavia initializada.';
'''

language = 'en';
vosk_model_path="/mnt/boveda/VOSK/vosk-model-small-en-us-0.15";
response_text='Yes. Can I help you?';
octavia_name='octavia';
initial_msg='octavia initialized.';


filename_tmp="temporal-file-trash.mp3"
sample_rate  =16000;
num_of_frames= 4000;
input_symbol='<<';
output_symbol='>>';
bypass_symbol='::';

################################################################################


 # Preparando o microfone para captura
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=sample_rate, input=True, frames_per_buffer=int(num_of_frames*2))
stream.start_stream()


# Apontando o algoritmo para ler o modelo treinado na pasta vosk_model_path
if not os.path.exists(vosk_model_path):
    msg="Model files path not exist:";
    print (msg)
    exit(1)
model = Model(vosk_model_path)
rec = KaldiRecognizer(model, sample_rate)

# Load the static command
static_class=processinglib.get_static_command_class_list(language,stream,filename_tmp); # classes
static_commands=[cls.get_text_command() for cls in static_class ];         # text commands

# Init message
speaklib.speak_the_text(stream,initial_msg,lang=language,ftemp=filename_tmp);
print(initial_msg);

enable_command=False;

while True:
    # Lendo audio do microfone
    data = stream.read(num_frames=num_of_frames);
    
    if rec.AcceptWaveform(data):
        cad=rec.Result();
        #print(cad)
        obj_dict = json.loads(cad);
        texto=obj_dict["text"].lower();
        
        if len(texto)>0:
            if (texto==octavia_name):
                print(input_symbol,texto);
                resposta=response_text;
                speaklib.speak_the_text(stream,resposta,lang=language,ftemp=filename_tmp);
                print(output_symbol,resposta)
                
                enable_command=True;
            
            elif enable_command==True:
                print(input_symbol,texto);
                if texto in static_commands:    # Execute command with literal text
                    ID=static_commands.index(texto);
                    static_class[ID].execute_command();
                else:                           # Analise the text and execute the processed information
                    processinglib.processing_command(texto,lang=language);
                enable_command=False;
            else:
                print(bypass_symbol,texto);
