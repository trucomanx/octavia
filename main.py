#!/usr/bin/python

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
import tools.init_work as iw
import tools.generic as tg

################################################################################
## VARIABLES 

init_data=dict();

init_json_file=iw.load_init_json_file('en');

with open(init_json_file, 'r') as fcc_file:
    init_data = json.load(fcc_file)

language       = init_data['language'];
vosk_model_path= init_data['vosk_model_path'];
response_text  = init_data['response_text'];
octavia_name   = init_data['octavia_name'];
initial_msg    = init_data['initial_msg'];

filename_tmp   = init_data['filename_tmp'];
sample_rate    = init_data['sample_rate'];
num_of_frames  = init_data['num_of_frames'];
input_symbol   = init_data['input_symbol'];
output_symbol  = init_data['output_symbol'];
bypass_symbol  = init_data['bypass_symbol'];

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
static_commands=[cls.get_text_command() for cls in static_class ];                      # text commands

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
                LID=tg.text_exist_in_double_list(texto,static_commands);
                if LID>=0:    # Execute command with literal text
                    ID=static_commands.index(static_commands[LID]);
                    static_class[ID].execute_command();
                else:         # Analise the text and execute the processed information
                    processinglib.processing_command(texto,lang=language);
                enable_command=False;
            else:
                print(bypass_symbol,texto);
