# transcribe-mp3
A script that takes all of the mp3 files in a directory, transcribes them into .txt files, and places them in an output directory. This is specifically useful for voice memos.


## Instructions

### Dependencies 

You need these python libraries (along with python 3):
- sys
- os
- subprocess
- json
- datetime
- vosk

### Installation of Model

The Vosk speech recognition API requires the use of a model. This is a usually a
40MB to 3GB zip file that gives the API what it needs to listen and interpret
speech. This [link](https://alphacephei.com/vosk/models) has a list of all
models compatible with the API. You can choose which one you would like to use
based on your use case.

After downloading your model of choice, unzip it and rename it "model." It needs
to be renamed model in order for the script to be able to find the model you
downloaded.
