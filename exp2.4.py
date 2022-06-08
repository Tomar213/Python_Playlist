# Write a Python program to replace last value of tuples in a list
lst = [(12,34,11),(29,33,1),(5,4)]
print([t[:-1]+(7,) for t in lst])



lst = [(12,34,11),(),(29,33,1),(5,4),()]
for item in lst:
    if len(item) ==0:
        lst.remove(item)
print("FINAL LIST: ",lst)



lst = [(12,12,12),(20,20,1),(5,4)]
i=1
for item in lst:
    sm  = 0
    mul =1
    for value in item:
        sm = sm +value
    print(f"sum of tuple {i} :",sm)
    for value in item:
        mul = mul*value 
    print(f"multiply of tuple {i}:",mul)  
    i += 1     
   
numb =("23","45","55")
print("Initially the tupple = ",numb)
for i in numb:
    print(type(i))
numb=tuple(map(int,numb))
print("After execution of map function: ",numb)
for i in numb:
    print(type(i))

tpl = [("karan","harry"),("sonal","ima"),("jazz","karan")]
serch = input("Enter your search: ")
i = 1
for item in tpl:
    for val in item:
        if val==serch :
            print(f"{serch} is in the Tuple{i}")
            break
    else:
            print(f"{serch} is NOT in the Tuple{i}")
    i +=1   


def duplicate(lst1):
    doc ={}
    for  item in lst:
        doc[item]=doc.get(item,0)+1
# print(doc)
    for k,v in doc.items():
        if v>1:
            print(f"Value {k} repeates {v} times")   

lst  = [120,600,200,409,600,600,400,500,400,120]
duplicate(lst)

lst  = [120,600,200,409,500,400,120]
# mul = 1
# for item in lst:
#     mul = mul*item
# print(mul)
lst.sort(reverse=True)
print("second largest",lst[-2])
print("Most smallest",lst[0])



d1 ={"karan":"sonal"}
l2 = []
for k,v in d1.items():
    for i in k:
        if i in v:
            print(f"common letter in {k} : {v} ",i) 
    for j in v:
        if j not in l2:
            l2.append(j)
print(l2)