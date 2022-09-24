#!/usr/bin/python

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

import tools.generic as tg

def execute_text_command(texto,static_commands,static_class,stream,language,filename_tmp):
    LID=tg.text_exist_in_double_list(texto,static_commands);
    if LID>=0:    # Execute command with literal text
        static_class[LID].execute_command();
    else:         # Analise the text and execute the processed information
        processing_command(texto,lang=language, stream=stream,ftemp=filename_tmp);
