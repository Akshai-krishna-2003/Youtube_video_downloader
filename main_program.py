import func as f
import time 
import os

while True:
##    try:
        print()
        print('Welcome to python youtube video downloader developed by Akshai krishna')
        print()
        menu=int(input('''
Menu of the program
~~~~~~~~~~~~~~~~~~~~
Press 0 to see the readme file of the program
Press 1 to see the details of that video
Press 2 to download highest resolution video
Press 3 to download lowest resolution video
Press 4 to download video of resolution you have given
Press 5 to download audio part of the video
Press 6 to download full video playlist
Press 7 to download full audio playlist
Press 8 to download part of playlist in video format
Press 9 to download part of playlist in audio format
Press 10 to exit the program

Enter your choice here : '''))
        print()

        if menu==0:
            time.sleep(2)
            with open('Readme.txt') as r:
                print(r.read())
            print()
            print('Moving back to menu again')
            time.sleep(2)

        elif menu==1:
            l=input('Copy and paste the url of the video here: ')
            f.v_details(l)
            print()
            print('Moving back to menu again')
            time.sleep(2)
                  
        elif menu==2:
            l,p=f.input_val()
            f.highest_resolution(l,p)
            print()
            print('Moving back to menu again')
            time.sleep(2)
                    
        elif menu==3:
            l,p=f.input_val()
            f.lowest_resolution(l,p)
            print()
            print('Moving back to menu again')
            time.sleep(2)

        elif menu==4:
            try:
                l,p=f.input_val()
                res=input('Enter the resolution that you want to download: ')
                f.own_resolution(l,res,p)
                print()
                print('Moving back to menu again')
                time.sleep(2)
            except:
                print()
                print('The resolution you have inputted may not be available')
                print('Going back to the menu again')
                time.sleep(2)

        elif menu==5:
            l,p=f.input_val()
            f.audio(l,p)
            print()
            print('Moving back to menu again')
            time.sleep(2)

        elif menu==6:
            l,p=f.input_valp()
            f.vid_playlist_full(l,p)
            print()
            print('All videos of the playlist has been downloaded')
            print('Moving back to menu again')
            time.sleep(2)

        elif menu==7:
            l,p=f.input_valp()
            f.audio_playlist_full(l,p)
            print()
            print('All audios of the playlist has been downloaded')
            print('Moving back to menu again')
            time.sleep(2)

        elif menu==8:
            l,p=f.input_valp()
            fr=int(input('Enter the beginning number of the video playlist you want: '))
            en=int(input('Enter the ending number of the video playlist you want: '))
            if fr>=en and fr<=0 and en<=0 and fr>len(urls) and en>len(urls):
                print('There is some error in the input')
                print()
                print('Moving back to menu again')
                continue
                time.sleep(2)
            else:
                f.vid_playlist_part(l,p,fr,en)
            print()
            print('Moving back to menu again')
            time.sleep(2)

        elif menu==9:
            l,p=f.input_valp()
            fr=int(input('Enter the beginning number of the audio playlist you want: '))
            en=int(input('Enter the ending number of the audio playlist you want: '))
            if fr>=en and fr<=0 and en<=0 and fr>len(urls) and en>len(urls):
                print('There is some error in the input')
                print()
                print('Moving back to menu again')
                continue
                time.sleep(2)
            else:
                f.audio_playlist_part(l,p,fr,en)
            print()
            print('Moving back to menu again')
            time.sleep(2)

        elif menu==10:
            inp=input('''
Are you sure you want to leave
Press y or Y to leave
Press anyother key to continue
Enter your choice here: ''')
            if inp=='y' or inp=='Y':
                print('Ending youtube video downloader program')
                time.sleep(5)
                break
            else:
                print('Continuing with the program')
                time.sleep(2)
                print()

        else:
            print('Invalid input , returning to main screen')
            print()
##    except:
##        print('Some Error has occured')
##        print('May be error with url or error with directory')
##        print('Please goback and check')
##        time.sleep(3)
##        print('Returning to main program')

    
