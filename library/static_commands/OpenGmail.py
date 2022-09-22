#!/usr/bin/python

#import os
import webbrowser
import speaklib

class OpenGmail:
    def __init__(self,lang,stream,tmpfile):
        self.lang = lang;
        self.stream=stream;
        self.tmpfile=tmpfile;
    
    def get_description(self):
        if(self.lang=='es'):
            return 'abre gmail en el navegador por defecto';
        else:
            return 'open gmail in the default web browser';
    
    def get_text_command(self):
        if(self.lang=='es'):
            return ['abre google mail','abre mi google mail','abre mi correo electrónico'];
        else:
            return ['open google gmail'];
    
    def execute_command(self):
        URL='http://gmail.com';
        webbrowser.open(URL) 
        
        if(self.lang=='es'):
            msg='Abriendo '+URL;
        else:
            msg='Opening '+URL;
        speaklib.speak_the_text(self.stream,msg,lang=self.lang,ftemp=self.tmpfile);
        return;
