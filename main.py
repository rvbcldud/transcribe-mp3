#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer, SetLogLevel
import sys
import os
import subprocess
import json
import datetime

SetLogLevel(0)

current_path = os.getcwd()
date = datetime.datetime.now().strftime("%Y%m%d")
output_path = "/output/" + date + "/"
rec_path = "/media/rvbcldud/IC RECORDER/REC_FILE/FOLDER01/"

final = ''

if not os.path.exists("model"):
    print ("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    exit (1)

# Create a way to transcribe the data with vosk-api

sample_rate=16000


# TODO create different paths for output ... whether there needs to be a "/" at
# the start of the path string
# TODO put user specific variable (e.g., directories, model)

# Function that opens an mp3 file through the console command "ffmpeg"

model = Model("model")

rec = KaldiRecognizer(model, sample_rate)

def open_mp3(sound_file):
    process = subprocess.Popen(['ffmpeg', '-loglevel', 'quiet', '-i',
                                sound_file,
                                '-ar', str(sample_rate) , '-ac', '1', '-f', 's16le', '-'],
                                stdout=subprocess.PIPE)
    return process

# Function that reads the file first opened by "ffmpeg" and then writes
# the transcription into a text file

def read_mp3(sound_file):
    final = ''
    while True:
        data = sound_file.stdout.read(2000)
        if len(data) == 0:
            print('break')
            break
        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())
            final = final + '...' + res['text']
    res = json.loads(rec.FinalResult())
    final = final + '...' + res['text']
    # Take everything before the person says "period" and make it the file name
    head, sep, tail = final.strip('...').partition('period')
    if not (os.path.isdir("output/" + date + "/")):
        os.mkdir("output/")
        os.mkdir("output/" + date + "/")
    print("output/" + date + "/" + head + ".txt")
    with open(("output/" + date + "/" + head + ".txt"), 'w') as f:
        # Write all of the transcription...minus whitespace at beggining
        f.write(final.strip())

for i in os.listdir(rec_path):
    read_mp3(open_mp3(rec_path + i))
