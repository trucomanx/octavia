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
import speaklib

def get_static_command_class_list(lang,stream,filename_tmp):
    relative_dir='static_commands';
    sc_path=os.path.join(os.path.dirname(__file__),relative_dir);
    class_list=[];
    for (dirpath, dirnames, filenames) in walk(sc_path):
        for fpath in filenames:
            basename=os.path.splitext(fpath)[0];
            cadena= relative_dir+'.'+basename+'.'+basename;
            print('Loading sub module:',cadena);
            klass = locate(cadena);
            class_list.append(klass(lang,stream,filename_tmp));
        break
    return class_list;


def processing_command(text,lang,stream,ftemp):
    if lang=='es':
        msg='comando no implementado: ';
    else:
        msg='command not implemented: ';
    speaklib.speak_the_text(stream,msg+text,lang=lang,ftemp=ftemp);
    print(">>",text);
    '''

    '''
