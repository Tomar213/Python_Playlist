# solution 1 
n=int(input("Enter a number "))
m=int(input("Enter 1 or 0 : "))
if m == 1:

    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end=" ") 
        print()

elif m== 0:
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print("*", end = " ")
        print()    

else :
    print("not valid")


#----------------------------------------------------------------------------------------------------------


#solution 2 
try:
    a= int(input("Enter a number : "))
    b= int(input("Enter 1 or 0 : "))

    if b == 1 :
        count = 0
        while (count <= a):
            print("* "*count)
            count  = count +1

    elif b== 0:
        count = a
        while (count !=0):
            print("* "*count)
            count = count -1 
    else:
        print('invalid')
except Exception as e :
    print(e)            