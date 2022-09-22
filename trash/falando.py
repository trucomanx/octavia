#!/usr/bin/python

# Import the required module for text 
# to speech conversion

import gtts

filename_tmp="temporal-file-trash.mp3"
    
# The text that you want to convert to audio
mytext = 'mande?'
  
# Language in which you want to convert
language = 'es'
  
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gtts.gTTS(text=mytext, lang=language, slow=False)
  
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save(filename_tmp)

#! pip3 install playsound
from playsound import playsound
playsound(filename_tmp);

# all available languages along with their IETF tag
#print(gtts.lang.tts_langs())
