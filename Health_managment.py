def getDate():
    import datetime
    return datetime.datetime.now()

#write functions
def diet_harry(o):
    h= str(getDate())
    f = open("diet_harry.txt","a")
    f.write("  \n")
    f.write(h)
    f.write("   ")
    f.write(o)
    f.close()

def exercise_harry(o):
    h= str(getDate())
    f = open("exercise_harry.txt","a")
    f.write("  \n")
    f.write(h)
    f.write("   ")
    f.write(o)
    f.close()

def diet_rohan(o):
    h= str(getDate())
    f = open("diet_rohan.txt","a")
    f.write("  \n")
    f.write(h)
    f.write("   ")
    f.write(o)
    f.close()

def exercise_rohan(o):
    h= str(getDate())
    f = open("exercise_harry.txt","a")
    f.write(h)
    f.write("   ")
    f.write(o)
    f.write("  \n")
    f.close()

def diet_hamad(o):
    h= str(getDate())
    f = open("diet_hamad.txt","a")
    f.write("  \n")
    f.write(h)
    f.write("   ")
    f.write(o)
    f.close()

def exercise_hamad(o):
    h= str(getDate())
    f = open("exercise_hamad.txt","a")
    f.write("  \n")
    f.write(h)
    f.write("   ")
    f.write(o)
    f.close()


#read functions
def E_harry():
    f=open("exercise_harry.txt")
    content = f.read()
    print(content)
    f.close()

def D_harry():
    f=open("diet_harry.txt")
    content = f.read()
    print(content)
    f.close()    

def D_rohan():
    f=open("diet_rohan.txt")
    content = f.read()
    print(content)
    f.close()

def D_hamad():
    f=open("diet_hamad.txt")
    content = f.read()
    print(content)
    f.close()   

def E_hamad():
    f=open("exercise_hamad.txt")
    content = f.read()
    print(content)
    f.close()  

def E_rohan():
    f=open("exercise_rohan.txt")
    content = f.read()
    print(content)
    f.close()


print('''press L To lock
Press R to retrieve ''')
n=input("What do you want to do retrieve or lock : ")
if n== "L":
    print('''press 1 for HARRY \nPress 2 for Rohan \nPress 3 for Hamad ''')
    m= int(input(" Choose out of 1 ,2, or 3  : "))
    if(m==1):
       print('''Press D for Diet \n press E for exercise ''' )
       p = input("ENTER D or E : ")
       if p=="D":
         o=  str(input("Enter Diet =  "))
         diet_harry(o)
         print("HARRY'S DIET LOCKED ......")
       elif p=="E":
           o= str(input("ENTER EXERCISE : "))
           exercise_harry(o)
           print("HARRY'S WORK ADDED........")
    elif(m==2):
       print('''press 1 for HARRY \nPress 2 for Rohan \nPress 3 for Hamad ''' )
       p = input("ENTER D or E : ")
       if p=="D":
         o=  str(input("Enter Diet =  "))
         diet_rohan(o)
         print("ROHAN'S DIET LOCKED ......")
       elif p=="E":
           o= str(input("ENTER EXERCISE : "))
           exercise_rohan(o)
           print("ROHAN'S WORK ADDED........")                
    elif(m==3):
       print('''press 1 for HARRY \nPress 2 for Rohan \nPress 3 for Hamad ''' )
       p = input("ENTER D or E : ")
       if p=="D":
         o=  str(input("Enter Diet =  "))
         diet_hamad(o)
         print("HAMAD'S DIET LOCKED ......")
       elif p=="E":
           o= str(input("ENTER EXERCISE : "))
           exercise_hamad(o)
           print("HAMAD'S WORK ADDED........")                  
elif(n=="R"):
    print('''press 1 for HARRY \nPress 2 for Rohan \nPress 3 for Hamad ''')
    m= int(input(" Choose out of 1 ,2, or 3  : "))
    if(m==1):
        print('''Enter D for diet \n E for exercise  ''')
        p = input("Enter D or E :")
        if(p=="E"):
            print("HARRY'S EXERCISES CHART ")
            E_harry()
        elif(p=="D"):
            print("HARRY'S DIET CHART")
            D_harry()
    elif(m==2):
        print('''Enter D for diet \n E for exercise  ''')
        p = input("Enter D or E :")
        if(p=="E"):
            print("ROHAN'S EXERCISES CHART ")
            E_rohan()
        elif(p=="D"):
            print("ROHAN'S DIET CHART ")
            D_rohan()        
    elif(m==3):
        print('''Enter D for diet \n E for exercise ''')
        p = input("Enter D or E :")
        if(p=="E"):
            print("HAMAD'S EXERCISES CHART ")
            E_hamad()
        elif(p=="D"):
            print("HAMAD'S DIET CHART ")
            D_hamad()  

     
        



                 

        
   
           
       

    