
import gtts
import os
from playsound import playsound

def speak_the_text(stream,resposta,lang='es',ftemp='temporal_file.mp3'):
    myobj = gtts.gTTS(text=resposta, lang=lang, slow=False)
    myobj.save(ftemp)
    
    stream.stop_stream()
    playsound(ftemp);
    os.remove(ftemp);
    stream.start_stream()

def speak_raw_the_text(resposta,lang='en',ftemp='temporal_file.mp3'):
    myobj = gtts.gTTS(text=resposta, lang=lang, slow=False)
    myobj.save(ftemp)
    playsound(ftemp);
    os.remove(ftemp);
