from pytubefix import YouTube
import moviepy.editor as ed
url = input('Enter the video url: ')
yt= YouTube(url)
streams = yt.streams
title = yt.title
choice = input('Video (V) or audio (A)? ')
try:
    if(choice == 'V' or choice == 'v'):
        streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first().download()
    elif (choice == 'A' or choice == 'a'):
        streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first().download()
        video = ed.VideoFileClip(title + '.mp4')
        video.audio.write_audiofile(title + '.mp3')
    else:
        print('Enter correct input')
except Exception as e:
    print('Exception has occured: ', e)
