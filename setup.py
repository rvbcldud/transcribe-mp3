from setuptools import setup

setup(name='Transcribe MP3',
    version='1.0',
    description='Transcribes all mp3 files in a specified directory',
    author='Ryan Vanden Bos',
    install_requires=['vosk'],
    packages=['transcribemp3'],
    entry_points={
        'console_scripts': ['transcribe-mp3=transcribemp3.main']
    }
)