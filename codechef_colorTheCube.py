import math
T = int(input("test cases:"))

while T>0:
    T=T-1
    costForOneDice=0
    N= int(input("No. of dice: "))
    for price in range(6):
        X =int(input(f"Rate of {price+1} paint:"))
        costForOneDice = costForOneDice+X
    print(f"Total cost of painting {N} cube: {costForOneDice*math.ceil((N*0.5))}")


#_______________soln by dhanesh___________________
import math
T=int(input())
lat=[]
while T>0:
    T=T-1
    st = input()
    b = list(map(int,st.split()))
    N=b[0]
    b.pop(0)
    cost = sum(b)*math.ceil(N*0.5)
    print(cost)


#____________________Q2_____________________
def check_copy(x):
    x=str(x)
    for i in x:
        if x.count(i) >1:
            return False
    else:
        return True
N= int(input())
while True:
    N=N+1
    if check_copy(N) ==True:
        print(N)
        break
    elif check_copy(N)==False:
        continue


        
