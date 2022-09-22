#!/usr/bin/python

#import os
import webbrowser
import speaklib
import processinglib

class ListStaticCommands:
    def __init__(self,lang,stream,tmpfile):
        self.lang = lang;
        self.stream=stream;
        self.tmpfile=tmpfile;
    
    def get_description(self):
        if(self.lang=='es'):
            return 'lista todos los comandos estáticos existentes';
        else:
            return 'list all existing static commands';
    
    def get_text_command(self):
        if(self.lang=='es'):
            return 'lista los comandos estáticos';
        else:
            return 'list the static commands';
    
    def execute_command(self):
        static_class=processinglib.get_static_command_class_list(self.lang,self.stream,self.tmpfile); # classes
        text_commands=[cls.get_text_command() for cls in static_class ];  # text commands 
        desc_commands=[cls.get_description() for cls in static_class ];  # text commands 
        
        for text,desc in zip(text_commands,desc_commands):
            if(self.lang=='es'):
                msg='comando: '+text;
            else:
                msg='command: '+text;
            speaklib.speak_the_text(self.stream,msg,lang=self.lang,ftemp=self.tmpfile);
            
            if(self.lang=='es'):
                msg='descripción: '+desc;
            else:
                msg='description: '+desc;
            speaklib.speak_the_text(self.stream,msg,lang=self.lang,ftemp=self.tmpfile);
        return;
