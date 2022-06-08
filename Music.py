from pygame import mixer
mixer.init()             #Starting the mixer  
mixer.music.set_volume(0.8)   

while True:
    print("Press A to play song1 --Press K to Play song2 -- P to pause -- C to continue -- E to exit")
    n = input()
    if n=="K":
        mixer.music.load("Ek_Chatur_Naar.mp3")      
        mixer.music.play()                  
        continue
    elif n=="A":
        mixer.music.load("aa1 (1).mp3")
        mixer.music.play()
        continue
    elif n =="P":
        mixer.music.pause()
        continue
    elif n=="C":
        mixer.music.unpause()
        continue
    else:
        mixer.music.stop()
        break        

