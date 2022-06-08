#Q1) Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
# import os
# from string import ascii_uppercase 
# first = input("Enter the first letter:")
# open("A.txt",'a')
# n= ord(first[0])
# for i in range(25):
#     n=n+1
#     first=chr(n)
#     f=open(f"{first}.txt","a")
#     print(first)

#Q2)Write a Python program to create a file where all letters of English alphabet are listed by specified number of letters on each line
f = open("letters.txt",'a')
import string
count = 0
for let in  string.ascii_uppercase:
    count+=1
    print(let,end=" ")
    f.write(f"{count}. {let}\n")
f.close()

#Q3) Write a Python program to read a random line from a file.
import random
r = random.randint(1,20)
f=open('project_twitter_data.csv')
lst = f.readlines()
print(f"RANDOMLY COMES LINE {r} \n{lst[r]}")
f.close()

#Q4  Write a Python program to count the frequency of words in a file
d1={}
with open('sonal.txt') as kar:
    cahracters = kar.read()
    for i in cahracters:
        if i =='\n' or i ==" ":
            pass
        else:
            d1[i]=d1.get(i,0)+1
# print(d1)
for key,val in d1.items():
    print(f"{key} occurs {val} times")
kar.close()

#Q5) Write a Python program to copy the contents of a file to another file
with open('karan.txt') as f1 , open('karan_new.txt','a') as f2:
    for line in f1:
        f2.write(line),
print("All lines copied succesfully")