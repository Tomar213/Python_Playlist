import os 

# print(os.listdir())

# print("hello world")
# str = "karan "
# str2 ='Singh '
# str3 = 'Tomar '
# r = str + str2 +str3 
# print(str[0:3]) 

n =input ("enter your name ")
print(f"GOOD MORNING {n} ")

d= input("Enter date : ")
letter = ''' hello |name| 
You are selected !

DATE = |date|
'''
letter = letter.replace("|name|",n)
letter = letter.replace("|date|",d)
print(letter)

#program to detect double spaces in a string
str  = "my opinon on this is  very limited"
doublespaces = str.find("  ")
print(doublespaces) 

#list in Python
l1= [1,54,2,3,56,32,5]
l1.insert(2,100)                #insert 100 at index 2
print(l1)

print(len(l1))

l1.reverse()    #reverse the elements of l1
print(l1)

l1.sort()           #sort elements in ascending order 
print(l1)

m1 = input("Enter Name of fruit 1 : ")
m2 = input("Enter Name of fruit 2 : ")
m3 = input("Enter Name of fruit 3 : ")
m4 = input("Enter Name of fruit 4 : ")
m5 = input("Enter Name of fruit 5 : ")
mylist = [m1,m2,m3,m4,m5]
print(mylist)


#Dictionary - Pair of words i.e 
d1 = {"karan":"java","Rohan":"Python","Raj":{"jassy":"flower","Lambo":"car"}}
print(d1["karan"])

d2= {"Python":"Marked 1 in easyness","Java":"Marked 1 in Programming","C++":"Data and Algorithm Understanding","HTML":"Best GUI Interface","Sql":"Database Perfection"}
n = input("Enter name of the language : ")
print(d2[n])

#if else
age= int(input("ENTER YOUR AGE : "))
if age > 18:
    print("You can Drive ")
elif age==18:
    print("WE CANNOT DECIDE , PLEASE VISIT US  PHYSICALLY ")
else:
    print("TOU CANNOT DRIVE")        


#for loop
l1  = ["harry ","garrry","larry","sunny"]
for  i in l1:
    print(i)

l1  = [["harry ",23,100],["garrry",67,200],["larry",23,250],["sunny",34,499]]
for  i,age,sal in l1:
    print(i,"'s age is",age,"and salary is",sal)


l2 = [23,5,"kar",100,"l",2,"pari"]
for i in l2:
    if str(i).isnumeric() and i>6:     # if it is a number and greater than 6
        print(i)


#while Loop 
while(True):
    n= int(input("ENTER YOUR NUMBER "))
    if n>100:
        print("you are welcome")
        break
    else:
        print("try again")
        continue



n = input("enter your name :")
count = 0

while(count <5):
    print(n)
    count = count +1 

#built in functions 
a= int(input("ENTER A = "))
b= int(input("ENTER B = "))
c= sum((a,b))
print("sum = ",c)


#user defined functions
def fun1():    
    print("you are in fun1 ")
    return 8
print(fun1())    
fun1()


def add(a,b):
    """this fuction will return the value of a+b"""     #doc string  i.e slight explaination or any note  to the fuction
    print("value is : ",a+b)
#add(3,4)   
print(add.__doc__)               #this will print the doc string


