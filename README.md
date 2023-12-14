# transcribe-mp3
A script that takes all of the mp3 files in a directory, transcribes them into .txt files, and places them in an output directory. This is especially useful for voice memos.


## Install

In order to install this package, type the following into the command line when at the project's directory:
```console
$ python3 setup.py install --user
```

You also need ffmpeg: ```sudo apt install ffmpeg```

### Installation of Model

The Vosk speech recognition API requires the use of a model. This is a usually a
40MB to 3GB zip file that gives the API what it needs to listen and interpret
speech. This [link](https://alphacephei.com/vosk/models) has a list of all
models compatible with the API. You can choose which one you would like to use
based on your use case.

After downloading your model of choice, unzip it and rename it "model". It needs
to be renamed model in order for the script to be able to find the model you
downloaded.

## Usage

### Choosing a key word

The program has been written so that when you say a certain word (that you
define) it takes everything before said word and makes it the title of the .txt
file. This word should not be a common word, such as "the," but it also
shouldn't be something too difficult to say and, consequently, for the program to
interpret. Therefore pick a simple, uncommon word to signal the end of the
title.

### Setting user-specific variables

After downloading a model and renaming it, you need to edit a file named
"info.json":
```json
{
    "rec_path":"/PATH/TO/RECORDINGS/",
    "key_word":"WORD THAT SIGNALS THE END OF THE TITLE"
}
```

### Running the program

After doing this and setting the variables appropriately, you can now run
the program: 
```console
$ transcribe-mp3
```

