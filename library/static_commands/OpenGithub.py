#!/usr/bin/python

#import os
import webbrowser
import speaklib

class OpenGithub:
    def __init__(self,lang,stream,tmpfile):
        self.lang = lang;
        self.stream=stream;
        self.tmpfile=tmpfile;
    
    def get_description(self):
        if(self.lang=='es'):
            return 'abre github en el navegador por defecto';
        else:
            return 'open github in the default web browser';
    
    def get_text_command(self):
        if(self.lang=='es'):
            return ['abre mi repositorio', 'abre el repositorio'];
        else:
            return ['open github','open my repostory','open the repostory'];
    
    def execute_command(self):
        URL='http://github.com';
        
        if(self.lang=='es'):
            msg='Abriendo github';
        else:
            msg='Opening github';
        speaklib.speak_the_text(self.stream,msg,lang=self.lang,ftemp=self.tmpfile);
        webbrowser.open(URL);
        return;
