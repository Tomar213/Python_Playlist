
x= 24
count = 0
while(count < 7):
    count = count +1 
    n=int(input("Enter number : "))
    if n==x:
        print("YOU WON ")
        break
    elif n>x:
        print("Greater")
    elif n<x :
        print("Lesser")  
    print((7-count),"Trials left")          
    
if count >= 7:
    print("YOU LOOSE ")

print("you took total",count ,"trials")   
