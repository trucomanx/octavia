#!/usr/bin/python

#import os
import webbrowser
import speaklib

class OpenWhatsapp:
    def __init__(self,lang,stream,tmpfile):
        self.lang = lang;
        self.stream=stream;
        self.tmpfile=tmpfile;
    
    def get_description(self):
        if(self.lang=='es'):
            return 'abre whatsapp en el navegador por defecto';
        else:
            return 'open whatsapp in the default web browser';
    
    def get_text_command(self):
        if(self.lang=='es'):
            return ['abre whatsapp','abre mi whatsapp'];
        else:
            return ['open whatsapp'];
    
    def execute_command(self):
        URL='https://web.whatsapp.com';
        
        if(self.lang=='es'):
            msg='Abriendo whatsapp';
        else:
            msg='Opening whatsapp';
        speaklib.speak_the_text(self.stream,msg,lang=self.lang,ftemp=self.tmpfile);
        webbrowser.open(URL);
        return;
