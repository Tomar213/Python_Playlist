# drink water = 35min
#eye exercise = 30 min
#physical exercise = 50 min

from pygame import mixer
import datetime
from time import time
def Song_loop(file , stopper):
    mixer.init()
    mixer.music.set_volume(0.9)
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = str(input("Type to Stop alarm : "))
        if a== stopper:
            mixer.music.stop()
            break     


def diet_harry(o):
    h= str(datetime.datetime.now())
    f = open("diet_harry.txt","a")
    f.write(f"\n{h}   {o}\n") 
    f.close()

w_time  = time()
e_time = time()
p_time = time()
while True:
    if time() - w_time > 5:
        print("Drink water ...................Type Drank")
        Song_loop("A_6.mp3","Drank")
        o="Drank water"
        diet_harry(o)
        w_time  = time()
    if time() - e_time > 12:
        print("Eye Exercise time ..................Type Eyes")
        Song_loop("aa1 (1).mp3","Eyes")
        o="Eyes done"
        diet_harry(o)
        e_time  = time()
    if time() - p_time > 20:
        print("Physical exercise time ..................Type Phy")
        Song_loop("Ek_Chatur_Naar.mp3","Phy")
        o="Exercise"
        diet_harry(o)
        p_time  = time()
