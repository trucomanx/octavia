#!/usr/bin/python

#import os
import webbrowser

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
            return 'abre google mail';
        else:
            return 'open google gmail';
    
    def execute_command(self):
        webbrowser.open('http://gmail.com') 
        
        return;
