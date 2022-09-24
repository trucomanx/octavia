#!/usr/bin/python

#import os
import webbrowser
import speaklib

class OpenSpotify:
    def __init__(self,lang,stream,tmpfile):
        self.lang = lang;
        self.stream=stream;
        self.tmpfile=tmpfile;
    
    def get_description(self):
        if(self.lang=='es'):
            return 'abre spotify en el navegador por defecto';
        else:
            return 'open spotify in the default web browser';
    
    def get_text_command(self):
        if(self.lang=='es'):
            return ['abre spotify'];
        else:
            return ['open spotify'];
    
    def execute_command(self):
        URL='https://open.spotify.com/search';
        
        if(self.lang=='es'):
            msg='Abriendo spotify';
        else:
            msg='Opening spotify';
        speaklib.speak_the_text(self.stream,msg,lang=self.lang,ftemp=self.tmpfile);
        webbrowser.open(URL);
        return;
