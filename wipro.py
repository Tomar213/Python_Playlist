input1 = input()
input2 = input()
st = input1+input2
lst =[]
for i in input1:
    if i not in input2 and i != ' ' and i not in lst:
        lst.append(i)
for i in input2 :
    if i not in input2 and i != ' ' and i not in lst:
        lst.append(i)
lst.sort()
print(lst)
for  i in lst:
    print(i,end="")


