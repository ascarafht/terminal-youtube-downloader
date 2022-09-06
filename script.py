#!/usr/bin/python3
from pytube import YouTube
from sys import argv
import os


FILE_PATH =  os.path.expanduser('~/Downloads/YouTube/')

link = argv[1]
yt = YouTube(link)

print("Downloading:", yt.title)
yd = yt.streams.get_highest_resolution()

yd.download(FILE_PATH)
print("Downloaded")