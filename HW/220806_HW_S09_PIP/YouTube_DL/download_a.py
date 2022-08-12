# coding: utf8
import youtube_dl 
import re

def worker(VID_ID):

	ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }],
        'postprocessor_args': [
            '-ar', '16000'
        ],
        'prefer_ffmpeg': True,
        'keepvideo': True
    }
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([VID_ID])