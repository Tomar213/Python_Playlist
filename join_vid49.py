lis = ["SRK","SALMAN","KATRINA","SUSHANT","RAJPUT"]

#lilke if we want to add "and" b/w the list elements 
a= " and ".join(lis)
print(f"{a} ARE BOLLYWOOD STARS ")

#seperate them with commas
a= ",  ".join(lis)
print(f"{a} and all the Bollywood makers")

#make elements of a list str to int
numb =["23","45","55"]
a=list(map(int,numb))
a[2]=a[2]+5
print(a)


#mapping elements of list 
nos = [2,3,5,44,25,10]
a= list(map(lambda x:x*x,nos))
print(a)