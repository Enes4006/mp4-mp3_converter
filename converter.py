'''

import subprocess

FFMPEG_PATH = r"C:/Users/ENES/Desktop/ffmpeg-8.0.1-essentials_build/bin/ffmpeg.exe"

def convert_video(input_file, output_file):
    command = [
        FFMPEG_PATH,
        "-i", input_file,
        output_file
    ]
    subprocess.run(command)

def convert_audio(input_file, output_file):
    command = [
        FFMPEG_PATH,
        "-i", input_file,
        output_file
    ]
    subprocess.run(command)

def extract_audio(video_file, audio_file):
    command = [
        FFMPEG_PATH,
        "-i", video_file,
        "-vn",
        "-acodec", "mp3",
        audio_file
    ]
    subprocess.run(command)


'''



import subprocess
import os
import sys
import tkinter as tk
from tkinter import filedialog, ttk
import threading
import re
import time


def get_ffmpeg_path():
    if getattr(sys, 'frozen', False):
        # EXE içindeyken
        base_path = sys._MEIPASS
    else:
        # Normal python çalışırken
        base_path = os.path.dirname(__file__)

    return os.path.join(base_path, "ffmpeg", "ffmpeg.exe")


FFMPEG_PATH = get_ffmpeg_path()


def convert_video(input_file, output_file):
    subprocess.run([FFMPEG_PATH, "-i", input_file, output_file])


def convert_audio(input_file, output_file):
    subprocess.run([FFMPEG_PATH, "-i", input_file, output_file])


def extract_audio(video_file, audio_file):
    subprocess.run([
        FFMPEG_PATH,
        "-i", video_file,
        "-vn",
        "-acodec", "mp3",
        audio_file
    ])
