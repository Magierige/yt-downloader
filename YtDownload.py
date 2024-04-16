from pytube import YouTube
from pytube import Playlist
import os
import random

def playlistDownload(p):
    print(f'Downloading: {p.title}')
    if type == 'a':
        for video in p.videos:
            print(f'Downloading: {video.title}')
            tempFile = video.streams.get_audio_only().download(output_path=f"Downloads/{p.title}")
            if os.path.exists(f"Downloads/{p.title}/{''.join(e for e in video.title if e.isalnum() or e.isspace())}.mp3"):
                num = random.randint(100, 999)
                os.rename(tempFile, f"Downloads/{p.title}/{''.join(e for e in video.title if e.isalnum() or e.isspace())} {num}.mp3")
            else:
                os.rename(tempFile, f"Downloads/{p.title}/{''.join(e for e in video.title if e.isalnum() or e.isspace())}.mp3")
            print(f'Downloaded: {video.title}')
    elif type == 'v':
        for video in p.videos:
            print(f'Downloading: {video.title}')
            video.streams.get_highest_resolution().download()
            print(f'Downloaded: {video.title}')
    else:
        print("Invalid type input")
        return
    print("Download is completed successfully")

def videoDownload(link):
    youtubeObject = YouTube(link)
    if type == 'a':
        youtubeObject = youtubeObject.streams.get_audio_only()
    elif type == 'v':
        youtubeObject = youtubeObject.streams.get_highest_resolution()
    else:
        print("Invalid type input")
        return
    try:
        print(f'Downloading: {youtubeObject.title}')
        tempFile = youtubeObject.download(output_path="Downloads")
    except:
        print("An error has occurred")
    if type == 'a':
        print(tempFile)
        os.rename(tempFile, f"Downloads/{''.join(e for e in youtubeObject.title if e.isalnum() or e.isspace())}.mp3")
    print("Download is completed successfully")

choice = input("Enter 'v' for video or 'p' for playlist: ")
if choice == 'v':
    link = input("Enter the YouTube video URL: ")
    type = input("Enter 'a' for audio or 'v' for video: ")
    videoDownload(link)
elif choice == 'p':
    link = input("Enter the YouTube playlist URL: ")
    type = input("Enter 'a' for audio or 'v' for video: ")
    playlist = Playlist(link)
    playlistDownload(playlist)