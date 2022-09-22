
import gtts
from playsound import playsound

def speak_the_text(stream,resposta,lang='es',ftemp='temporal_file.mp3'):
    myobj = gtts.gTTS(text=resposta, lang=lang, slow=False)
    myobj.save(ftemp)
    
    stream.stop_stream()
    playsound(ftemp);
    stream.start_stream()
