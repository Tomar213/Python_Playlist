
import os

def setFiles(pat,file ,type):
    # os.chdir(path)
    files = os.listdir(pat)
    j=1
    f = open(file,'w+')
    filelist = f.read()
    for file in files:
        if file not in filelist:
            os.rename(file,file.capitalize())
        if os.path.splitext(file)[1]==type:
            print(os.rename(file,f"{j}{type}"))
            
            j +=1


setFiles("F://testing","F://sem04//new.txt",".png")

