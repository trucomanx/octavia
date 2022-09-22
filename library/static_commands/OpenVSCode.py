#!/usr/bin/python

import os


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
            return 'abre visual studio code';
        else:
            return 'open visual studio code';
    def execute_command(self):
        os.system('code') 
        
        return;
