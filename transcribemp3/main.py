import datetime
import json
import os
import subprocess

from vosk import KaldiRecognizer, Model, SetLogLevel

# Store the date in YEAR|MONTH|DAY format into date variable
date = datetime.datetime.now().strftime("%Y%m%d")

# Open JSON file with user-specific data
json_info = open("info.json")
variables = json.load(json_info)

# Retrieve the path of the recordings and key word
rec_path = variables["rec_path"]
key_word = variables["key_word"]

# This is where the final .txt files will go
output_path = "output/" + date + "/"

# Checks if user has downloaded a model from vosk
if not os.path.exists("model"):
    print(
        "Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder."
    )
    exit(1)

# Opens model and creates KaldiRecognizer object to interpret speech
sample_rate = 16000
model = Model("model")
rec = KaldiRecognizer(model, sample_rate)


# Function that opens an mp3 file through the console command "ffmpeg"
def open_mp3(sound_file):
    process = subprocess.Popen(
        [
            "ffmpeg",
            "-loglevel",
            "quiet",
            "-i",
            sound_file,
            "-ar",
            str(sample_rate),
            "-ac",
            "1",
            "-f",
            "s16le",
            "-",
        ],
        stdout=subprocess.PIPE,
    )
    return process


# Function that reads the file first opened by "ffmpeg" and then writes
# the transcription into a text file
def read_mp3(sound_file):
    final = ""
    while True:
        data = sound_file.stdout.read(2000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())
            final = final + "..." + res["text"]
    res = json.loads(rec.FinalResult())
    final = final + "..." + res["text"]
    # Take everything before the person says the key word defined in JSON file
    # and make it the file name
    head, sep, tail = final.strip("...").partition(key_word)
    if not (os.path.isdir(output_path)):
        os.mkdir(output_path)
    print(output_path + head + ".txt")
    with open((output_path + head + ".txt"), "w") as f:
        # Write all of the transcription...minus whitespace at beggining
        f.write(final.strip())

# Iterates through each recording in given path and outputs .txt files
for i in os.listdir(rec_path):
    read_mp3(open_mp3(rec_path + i))
    os.remove(rec_path + i)
