#!/usr/bin/python

import os
import sys
import speaklib

class OpenTextEditor:
    def __init__(self,lang,stream,tmpfile):
        self.lang = lang;
        self.stream=stream;
        self.tmpfile=tmpfile;
    
    def get_description(self):
        if(self.lang=='es'):
            return 'innecesaria';
        else:
            return 'not necessary';
    
    def get_text_command(self):
        if(self.lang=='es'):
            return ['abre el editor de texto'];
        else:
            return ['open the text editor'];
    
    def execute_command(self):
        if( sys.platform=='linux'):
            os.system('gedit');
        elif( sys.platform=='win32'):
            os.system('notepad');
        else:
            os.system('gedit');
        
        if(self.lang=='es'):
            msg='Abriendo editor de texto';
        else:
            msg='Opening editor de texto';
        speaklib.speak_the_text(self.stream,msg,lang=self.lang,ftemp=self.tmpfile);
        return;
