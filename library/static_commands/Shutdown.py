#!/usr/bin/python

import os
import sys
import speaklib

class Shutdown:
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
            return ['desconecta la computadora'];
        else:
            return ['shutdown the computer'];
    
    def execute_command(self):
        if( sys.platform=='linux'):
            os.system("shutdown -P");
        elif( sys.platform=='win32'):
            os.system("shutdown  /s /t 3");
        else:
            os.system("shutdown -P");
        
        if(self.lang=='es'):
            msg='Lanzado comando de apagado';
        else:
            msg='launch shutdown command';
        speaklib.speak_the_text(self.stream,msg,lang=self.lang,ftemp=self.tmpfile);
        return;
