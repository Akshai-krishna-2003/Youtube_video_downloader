import pytube
from pytube import YouTube
from pytube.streams import Stream
from pytube.cli import on_progress
import time
from pytube import Playlist
import os

def highest_resolution(l,p='.'):
    print()
    yt=YouTube(l,on_progress_callback=on_progress)
    time.sleep(2)
    print('Searching your video')
    st=yt.streams.get_highest_resolution()
    st.download(p)
    print()
    print('Downloaded the video')

def lowest_resolution(l,p='.'):
    print()
    yt=YouTube(l,on_progress_callback=on_progress)
    time.sleep(2)
    print('Searching your video')
    st=yt.streams.get_lowest_resolution()
    st.download(p)
    print()
    print('Downloaded the video')

def own_resolution(l,res,p='.',):
    print()
    yt=YouTube(l,on_progress_callback=on_progress)
    time.sleep(2)
    print('Searching your video')
    st=yt.streams.filter(res=res).first()
    st.download(p)
    print()
    print('Downloaded the video')

def v_details(l):
    print()
    yt=YouTube(l)
    d={'title' : yt.title,
        'owner' : yt.channel_id ,
        'length' : yt.length,
        'date' : yt.publish_date,
        'rate' : yt.rating,
        'view' : yt.views,
        'hfs' : yt.streams.get_highest_resolution().filesize,
        'lfs' : yt.streams.get_lowest_resolution().filesize}
    print('''
Details of the video
--------------------
url of the video               : {}
Title of the video             : {}
Owner ID of the video          : {}
Length of the video            : {} minutes
Date of publish                : {} 
Ratings of the video           : {}
Views of this video            : {} people have watched this video
Filesize of highest resolution : {} MB
Filesize of lowest resolution  : {} MB
'''.format(l,d['title'],d['owner'],d['length']/60 ,d['date'],d['rate'],d['view'] ,d['hfs']/1048576 ,d['lfs']/1048576))

def audio(l,p='.'):
    print()
    yt=YouTube(l,on_progress_callback=on_progress)
    time.sleep(2)
    print('Searching for that audio')
    st=yt.streams.filter(only_audio=True).first()
    st.download(p)
    print()
    print('Downloaded the audio of that video')

def vid_playlist_full(l,p):
    print()
    inp=int(input('''
Whether you want all playlist videos as
Press 1 for high quality video
Press 2 for low quality video

Enter your choice here: '''))
    pl=Playlist(l)
    urls=pl.video_urls
    print('Number of videos in this playlist is {}'.format(len(urls)))
    if inp==1:
        x=1
        for url in urls:
            print()
            yt=YouTube(url,on_progress_callback=on_progress)
            time.sleep(2)
            print('Searching video {}'.format(x))
            st=yt.streams.get_highest_resolution()
            out_file=st.download(p)
            base, ext = os.path.splitext(out_file)
            new_file = base + ' Video {}'.format(x) + '.mp4'
            os.rename(out_file, new_file)
            print()
            print('Video number {} has been downloaded'.format(x))
            print()
            x+=1
    elif inp==2:
        x=1
        for url in urls:
            print()
            yt=YouTube(url,on_progress_callback=on_progress)
            time.sleep(2)
            print('Searching your video {}'.format(x))
            st=yt.streams.get_lowest_resolution()
            out_file=st.download(p)
            base, ext = os.path.splitext(out_file)
            new_file = base + ' Video {}'.format(x) + '.mp4'
            os.rename(out_file, new_file)
            print()
            print('Video number {} has been downloaded'.format(x))
            print()
            x+=1
    else:
        print('Invalid input , returning to main program')

def audio_playlist_full(l,p):
    print()
    pl=Playlist(l)
    urls=pl.video_urls
    print('Number of audios in this playlist is {}'.format(len(urls)))
    print()
    x=1
    for url in urls:
        yt=YouTube(url,on_progress_callback=on_progress)
        time.sleep(2)
        print('Searching for audio {}'.format(x))
        st=yt.streams.filter(only_audio=True).first()
        out_file=st.download(p)
        base, ext = os.path.splitext(out_file)
        new_file = base + ' Audio {}'.format(x) + '.mp3'
        os.rename(out_file, new_file)
        print()
        print('Audio number {} has been downloaded'.format(x))
        print()
        x+=1

def vid_playlist_part(l,p,fr,en):
    print()
    inp=int(input('''
Whether you want all playlist videos as
Press 1 for high quality video
Press 2 for low quality video

Enter your choice here: '''))
    print()
    pl=Playlist(l)
    urls=pl.video_urls
    print('Number of videos in this playlist is {}'.format(len(urls)))
    print()
    if inp==1:
        for i in range(fr-1,en):
            url=urls[i]
            yt=YouTube(url,on_progress_callback=on_progress)
            time.sleep(2)
            print('Searching video {}'.format(i+1))
            st=yt.streams.get_highest_resolution()
            out_file=st.download(p)
            base, ext = os.path.splitext(out_file)
            new_file = base + ' Video {}'.format(i+1) + '.mp4'
            os.rename(out_file, new_file)
            print()
            print('Video number {} has been downloaded'.format(i+1))
            print()
    elif inp==2:
        for i in range(fr-1,en):
            url=urls[i]
            yt=YouTube(url,on_progress_callback=on_progress)
            time.sleep(2)
            print('Searching video {}'.format(i+1))
            st=yt.streams.get_lowest_resolution()
            out_file=st.download(p)
            base, ext = os.path.splitext(out_file)
            new_file = base + ' Video {}'.format(i+1) + '.mp4'
            os.rename(out_file, new_file)
            print()
            print('Video number {} has been downloaded'.format(i+1))
            print()
    else:
        print('Invalid input , returning to main program')

def audio_playlist_part(l,p,fr,en):
    print()
    pl=Playlist(l)
    urls=pl.video_urls
    print('Number of audios in this playlist is {}'.format(len(urls)))
    print()
    for i in range(fr-1,en):
        url=urls[i]
        yt=YouTube(url,on_progress_callback=on_progress)
        time.sleep(2)
        print()
        print('Searching for audio {}'.format(i+1))
        st=yt.streams.filter(only_audio=True).first()
        out_file=st.download(p)
        base, ext = os.path.splitext(out_file)
        new_file = base + ' Audio {}'.format(i+1) + '.mp3'
        os.rename(out_file, new_file)
        print()
        print('Audio number {} has been downloaded'.format(i+1))

def input_val():
    print()
    l=input('Copy and paste the url of the video here: ')
    an=input('''
Do you want to download your video in a directory that you wish
if yes press y or Y
press anyother key to download in default directory
Enter your choice: ''')
    print()
    if an=='y' or an=='Y':
        p=input('Enter the directory here: ')
        print()
    else:
        p='.'
    return l,p

def input_valp():
    print()
    l=input('Copy and paste the url of the playlist here: ')
    an=input('''
Do you want to download your playlist in a directory that you wish
if yes press y or Y
press anyother key to download in default directory
Enter your choice: ''')
    print()
    if an=='y' or an=='Y':
        p=input('Enter the directory here: ')
        print()
    else:
        p='.'
    return l,p


if __name__=='__main__':
    print('This file is not meant for execution')
    print('File name main_program.py is meant for execution')
    

