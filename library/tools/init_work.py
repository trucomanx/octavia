#!/usr/bin/python

from pathlib import Path
import os
import shutil
import speaklib

def load_init_json_file(lang_default='en'):
    home = str(Path.home())
    fpath=os.path.join(home,'octavia.json');
    if os.path.isfile(fpath):
        msg='It was loaded the init file : '+fpath;
        speaklib.speak_raw_the_text(msg,lang='en');
        return fpath;
    else:
        fsource=os.path.dirname(__file__);
        fsource=os.path.join(fsource,'..','..','octavia.'+lang_default+'.json');
        shutil.copy(fsource,fpath);
        
        if os.path.isfile(fpath):
            msg='It was created the init file : '+fpath;
            speaklib.speak_raw_the_text(msg,lang='en');
            return fpath;
        else:
            msg='Error loading the init file: '+fpath;
            speaklib.speak_raw_the_text(msg,lang='en');
            sys.exit(msg);
