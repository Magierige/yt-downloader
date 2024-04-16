from pytube import YouTube
from pytube import Playlist
import os
import random

def playlistDownload(p):
    print(f'Downloading: {p.title}')
    if type == 'a':
        for video in p.videos:
            tempFile = video.streams.get_audio_only().download(output_path=f"Downloads/{p.title}")
            if os.path.exists(f"Downloads/{p.title}/{video.title.replace("/", " ")}.mp3"):
                num = random.randint(100, 999)
                os.rename(tempFile, f"Downloads/{p.title}/{video.title.replace("/", " ")} {num}.mp3")
            else:
                os.rename(tempFile, f"Downloads/{p.title}/{video.title.replace("/", " ")}.mp3")
    elif type == 'v':
        for video in p.videos:
            video.streams.get_highest_resolution().download()
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
        # Download the video in a subdirectory called "Downloads"\
        tempFile = youtubeObject.download(output_path="Downloads")
    except:
        print("An error has occurred")
    if type == 'a':
        # Rename the file to the title of the video
        print(tempFile)
        os.rename(tempFile, f"Downloads/{youtubeObject.title.replace("/", " ")}.mp3")
    print("Download is completed successfully")

# user input to choose between video or playlist
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