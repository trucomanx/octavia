#!/usr/bin/python

import os

class Restart:
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
            return 'reinicia la computadora';
        else:
            return 'restart the computer';
    
    def execute_command(self):
        if( sys.platform=='linux'):
            os.system("shutdown -r");
        elif( sys.platform=='win32'):
            os.system("shutdown  /r /t 3");
        else:
            os.system("shutdown -r");
        
        return;
