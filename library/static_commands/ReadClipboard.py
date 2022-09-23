#!/usr/bin/python

#import os
#import webbrowser
import speaklib
import xerox #sudo apt-get install xclip

class ReadClipboard:
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
            return ['lee el portapapeles','lee el contenido del portapapeles'];
        else:
            return ['read the clipboard'];
    
    def execute_command(self):
        msg=xerox.paste();
        #print(msg)
        speaklib.speak_the_text(self.stream,msg,lang=self.lang,ftemp=self.tmpfile);
        return;
