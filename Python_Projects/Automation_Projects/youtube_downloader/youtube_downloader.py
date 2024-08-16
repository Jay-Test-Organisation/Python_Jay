# from pytube import YouTube
# The above was supposed to work but gave 400 error so using the below library
from pytubefix import YouTube
from pytubefix.cli import on_progress
from sys import argv

link = argv[1]
yt = YouTube(link)

print ("Title:", yt.title)
print ("View:", yt.views)

yd = yt.streams.get_lowest_resolution()

yd.download("C:\\Users\\Admin\\Desktop\\Git\\python\\Python_Projects\\Automation_Projects\\youtube_downloader")


# RUN python .\youtube_downloader.py "https://www.youtube.com/watch?v=vEQ8CXFWLZU"


