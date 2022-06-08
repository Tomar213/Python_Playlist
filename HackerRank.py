# a = int(input())
# b = int(input())
# print(a//b)
# print(a/b)

# n = int(input())
# for i in range(n):
#     print(i*i)


# def is_leap(year):
#     leap = False
#     if (year%4 == 0):
#         leap = True
#         if (year%100 ==0 and year%400 ==0 ):
#            leap =  True
#         elif (year%100==0):
#             leap = False
#     return leap
# yr = int(input())
# print(is_leap(yr))

# n = int(input())
# for i in range(n):
#     print(i+1,end="")

# n = int(input())
# st = set()
# for i in range(n):
#     ele = input()
#     st.add(ele)
# print(st)
# print(len(st))

# n = int(input("no. of elements: "))
# s = set(map(int, input("enter elements: ").split()))
# N = int(input("Number of functions: "))
# for i in range(N):
#     fun = input("Enter func. : ").split()
#     if fun[0] == "remove":
#         s.remove(int(fun[1]))
#     elif fun[0]=="discard":
#         s.discard(int(fun[1]))
#     elif fun[0]=="pop":
#         s.pop()
# print(s)

# x= int(input("x: "))
# y= int(input("y: "))
# z= int(input("z: "))
# n= int(input("n: "))
# lst2 = list()
# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             lst = [i,j,k]
#             # print(lst)
#             if sum(lst)!=n:
#                 lst2.append(lst)
# print(lst2)

# n = int(input())
# str = list(map(int,input().split()))
# str.sort(reverse=True)
# print(str)
# for i in str:
#     if str[0]!=i:
#         print(i)
#         break


# def srt(ary):
#     return ary[-1]
# lst = list()
# n = int(input("n "))
# for i in range(n):
#     nm = input("enter name ")
#     grade = float(input("grade "))
#     lit =[nm,grade]
#     lst.append(lit)
# # print(lst)
# lst2 = sorted(lst,key=srt)
# # print(lst2)
# final_list=[]
# for i in lst2:
#     if i[1]>lst2[0][1]:
#         # print(i[0],i[1])
#         temp = i[1]
#         for j in lst2:
#             if j[1]==temp:
#                 # print(j[0])
#                 final_list.append(j[0])                
#         break
# final_list.sort()
# for name in final_list:
#     print(name)


# n = int(input())
# student_marks = {}
# for i in range(n):
#     line = input().split()
#     name = line[0]
#     line.pop(0)
#     scores = list(map(float, line))
#     student_marks[name] = scores
# query_name = input()
# if query_name in student_marks.keys():
#     print("{:.2f}".format(sum(student_marks[query_name])/3))
# else: print(f"{query_name} not found in dictionary")



def uid_check(st):
    numCnt =0
    strCnt = 0
    upperCnt =0
    if len(st)==10:
        for i in st:
            if st.count(i)>1:
                print(f"Invalid")
                return
            try:
                i = int(i)
            except: i= i
            if type(i) is int:
                numCnt+=1
            elif type(i)is str:
                if i == i.lower():
                    strCnt+=1
                if i == i.upper():
                    upperCnt+=1
    else:
        print("Invalid") 
        return       
    # print(f"Number of int {numCnt} , number of small alphabet: {strCnt}, uppercase: {upperCnt}" )

    if numCnt<3:
        print("Invalid")
        return
    elif upperCnt<2:
        print("Invalid")
        return
    else:
        print("Valid")
     
N =int(input())
while N>0:
    N-=1
    uid = input()
    uid_check(uid)


