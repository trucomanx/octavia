#!/usr/bin/python

# abre gmail
# abre navegador
# reinicia
# desconecta 
# busca en google :: texto
# bloquea pantalla
# executa musica

import os
from os import walk

from pydoc import locate


def get_static_command_class_list(lang,stream,filename_tmp):
    base_dir='static_commands';
    sc_path=os.path.join(os.path.dirname(__file__),base_dir);
    class_list=[];
    for (dirpath, dirnames, filenames) in walk(sc_path):
        for fpath in filenames:
            basename=os.path.splitext(fpath)[0];
            cadena= base_dir+'.'+basename+'.'+basename;
            print('Loading sub module:',cadena);
            klass = locate(cadena);
            class_list.append(klass(lang,stream,filename_tmp));
        break
    return class_list;


def processing_command(text,lang='es'):
    print(">>",text);
    '''
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
    '''
