a = int(input("Enter a : "))
b= int(input("Enter b : "))
c = input("select an opertator(%,/,+,-,*) : ")

if(a==45 and b==3 and c=="*"):
    print(555)
elif(a==56 and b==9 and c=="+") :
    print(77)   
elif(a==56 and b==6 and c=="/"):
    print(4)    
elif(c== "*"):
    d= a*b
    print("Result : ",d)      
elif(c=="+"):
    d=a+b
    print("Result : ",d)      
elif(c=="-"):
    d=a-b
    print("Result : ",d)      
elif(c=="/"):
    d= a/b
    print("Result : ",d)     
elif(c=="%"):
    d= a%b
    print("Result : ",d)  
else:
    print("invalid")



       
