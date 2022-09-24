# Octavia
Octavia is a voice-controlled virtual assistant

# Execute

    python3 main.py

# Current static commands
These are commands that match exact text, without text interpretation.

    python3 main.py --list-static-commands

# Install

## Requirements
Install the required python modules:

    pip3 install -r requirements.txt

in windows also need 

    pip3 install -r requirements.win32.txt


### Requirements in Ubuntu

    xargs sudo apt-get install < packages.txt

## Download VOSK model 

Download a vosk model from:

    https://alphacephei.com/vosk/models

Later, unzip the model in some subdirectory in `/path/of/model`.

## Modifying the octavia configuration file

Modified or create the `octavia.json` in the `home` user directory.
The `octavia.json` should be have the next structure:

    {
        "language" : "en",
        "vosk_model_path":"/path/of/model/vosk-model-small-en-us-0.15",
        "response_text":"Yes. Can I help you?",
        "octavia_name":"octavia",
        "initial_msg":"octavia initialized.",
        "filename_tmp":"temporal-file-trash.mp3",
        "sample_rate"  : 16000,
        "num_of_frames":  4000,
        "input_symbol":"<<",
        "output_symbol":">>",
        "bypass_symbol":"::"
    }



