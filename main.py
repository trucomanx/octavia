#!/usr/bin/python

import sys 
import os

lib_path=os.path.join(os.path.dirname(__file__),'library');
sys.path.append(lib_path)

################################################################################

# externas
from vosk import Model, KaldiRecognizer
import pyaudio
import json


# propia
import speaklib
import processinglib
import tools.init_work as iw

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

################################################################################
# Load the static command
print('\n')
static_class=processinglib.get_static_command_class_list(language,stream,filename_tmp); # classes
static_commands    =[cls.get_text_command() for cls in static_class ];                  # text commands
static_descriptions=[cls.get_description() for cls in static_class ];                   # text description

if '--list-static-commands' in sys.argv:
    print('')
    print('COMMAND LIST')
    print('============')
    print('')
    for n in range(len(static_descriptions)):
        print('   commands: ',static_commands[n])
        print('description: ',static_descriptions[n])
        print('');
    sys.exit('');

################################################################################

# Apontando o algoritmo para ler o modelo treinado na pasta vosk_model_path
if not os.path.exists(vosk_model_path):
    msg="Model files path not exist:";
    print (msg)
    exit(1)
model = Model(vosk_model_path)
rec = KaldiRecognizer(model, sample_rate)

################################################################################

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
            if texto.startswith(octavia_name):
                nn=len(octavia_name);
                print(input_symbol,texto);
                if(octavia_name==texto):
                    resposta=response_text;
                    speaklib.speak_the_text(stream,resposta,lang=language,ftemp=filename_tmp);
                    print(output_symbol,resposta)
                    enable_command=True;
                else:
                    texto=texto[nn:].strip();
                    processinglib.execute_text_command( texto,static_commands,static_class,stream,language,filename_tmp);
                    enable_command=False;
            
            elif enable_command==True:
                print(input_symbol,texto);
                processinglib.execute_text_command( texto,static_commands,static_class,stream,language,filename_tmp);
                enable_command=False;
            
            else:
                print(bypass_symbol,texto);
