# QUE) You are given T testcases , each testcase consists of 3 numbers , P,X,Y,Z.
# You have a best friend named Rahul. Z is 1 if you will meet Rahul and 0 otherwise.
#  You initially has an Emotional Proximity of P, which increases by Y% if you meet
#   Rahul and decreases by X% otherwise. You have to print the final Emotional Proximity.  

T= int(input("Test case:"))
while T>0:
    T=T-1
    valus = input("Enter the 4 values (P X Y Z):")
    lst = list(map(int,valus.split()))
    if(lst[len(lst)-1]==0):
        p = (lst[0]*lst[1])/100
        print(lst[0]-p)
    else:
        p = (lst[0]*lst[2])/100
        print(lst[0]+p)
