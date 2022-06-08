# N =int(input())
# mylist =[]
# for i in range(N):
#     cmd = input().split()
#     if cmd[0]=='insert':
#         mylist.insert(int(cmd[1]),int(cmd[2]))
#     elif cmd[0]=='print':
#         print(mylist)
#     elif cmd[0] =='remove':
#         try:
#             mylist.remove(int(cmd[1]))
#         except:
#             pass
#     elif cmd[0] =='append':
#         mylist.append(int(cmd[1]))
#     elif cmd[0] =='sort':
#         mylist.sort()
#     elif cmd[0]=='pop':
#         mylist.pop()
#     elif cmd[0]=='reverse':
#         mylist.reverse()

# t1 = tuple()
# N = int(input())
# integer_list = tuple(map(int, input().split()))
# print(integer_list)
# print(hash(integer_list))


# import re
# N=int(input())
# while N >0:
#     N-=1
#     pattern = input()
#     try:
#         re.compile(pattern)
#         print("Valid")
#     except:
#         print("Not valid")

def pan_card(numb):
    if len(numb)!=16:
        print("Not Valid")
        return
    else:
        