#!/usr/bin/python

import os
import speaklib

class OpenVSCode:
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
            return ['abre visual studio code'];
        else:
            return ['open visual studio code'];
    def execute_command(self):
        os.system('code') 
        
        if(self.lang=='es'):
            msg='Abriendo visual studio code';
        else:
            msg='Opening visual studio code';
        speaklib.speak_the_text(self.stream,msg,lang=self.lang,ftemp=self.tmpfile);
        
        return;
