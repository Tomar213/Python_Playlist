def check(a,b,c):
    if  a+b+c == 0:
        return 0
    elif a-b+c == 0:
        return 0 
    elif a+b-c == 0:
        return 0
    elif -a+b-c == 0:
        return 0
    elif a-b+c == 0:
        return 0
    elif -a-b-c == 0:
        return 0
    elif -a-b+c == 0:
        return 0 
    elif -a+b+c == 0:
        return 0 
    else:
        return 1

T = int(input())
while T>0:
    T=T-1
    nos = input()            #enter space separated values of a, b and c
    lst = list(map(int,nos.split()))
    if check(lst[0],lst[1],lst[2])==0:
        print("YES")
    else:
        print("NO")  



#Practice set questions -
# q1 Good weather or not ,1 = sunny day , 0 = rainy day , good weather is no of days of sunn are more
T = int(input())
while T> 0 :
    T -=1
    val = input()                      #enter space separated values 1 or 0 seven times
    lst = list(map(int,val.split()))
    if lst.count(1)>lst.count(0):
        print("Weather is good")
    else:
        print("Not good weather")

#q2- the preparation , test is after M min , total episodes = N, Time of each episode = K min
T = int(input())
while T > 0 :
    T-=1
    info = input()                   #enter space separated values of M N K
    l = list(map(int,info.split()))
    if((l[1]*l[2])>=l[0]):
        print("No")
    else:
        print("Yes")

T =int(input())
while T>0:
    T-=1   
    l = list(map(int,input().split()))
    if l[1]> ((l[2]*2)+l[0]):
        print("No")
    else:
        print("Yes")