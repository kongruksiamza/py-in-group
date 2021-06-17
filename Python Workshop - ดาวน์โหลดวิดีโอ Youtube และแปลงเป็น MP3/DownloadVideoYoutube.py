from __future__ import unicode_literals
import youtube_dl

text=input("Insert Youtube Link:")
ydl = youtube_dl.YoutubeDL({'outtmpl': '%(title)s%(ext)s'})

with ydl:
    result = ydl.extract_info(
        text,
        download=True
    )
