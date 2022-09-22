#!/usr/bin/python

#import os
import webbrowser

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
            return 'abre mi repositorio';
        else:
            return 'open github';
    
    def execute_command(self):
        webbrowser.open('http://github.com') 
        
        return;
