from numpy import integer


fil = open("olymbian.csv","a")
contents = [("Abhinav",19,"football"),("t",202,"swimhgfgdfsang"),("Nimbu",19,"golf")]
fil.write(f"Name,Age,Sport")
fil.write("\n")
for content in contents:
    fil.write(f"{content[0]},{content[1]},{content[2]}\n")
fil.close()


fil2 = open("karan.txt")
content = fil2.read()
num=0
for character in content:
    num+=1
    print(character,end=" ")
print(num)
fil2.close()



fil2 = open("karan.txt")
# content = fil2.read()
cnt =0
words =[]
for line in fil2:
    newline= line.split(" ")
    cnt =cnt+ len(newline)
print(cnt)
fil2.close()

fil2 = open("karan.txt")
num_line=0
for line in fil2:
    num_line+=1
print(num_line)
fil2.close()


fil2 = open("karan.txt")
content = fil2.read()
begin_char = content[:30]
print(begin_char)
# for cahr in content[:10]:
#     print(cahr,type(cahr))
fil2.close()

three=[]
fil2 = open("karan.txt")
for line in fil2:
    newline = line.split(" ")
    three.append(newline[0])
print(three)
fil2.close()


p_words = list()
fil = open("karan.txt")
for line in fil:
    newline = line.strip("\n")
    newline = newline.split(" ")
    for word in newline:
        if "p" in word:
            p_words.append(word)
print(p_words)
fil.close()


list_of_price = []
list_of_intererst = []
fil3 = open("SP500.txt")
for line in fil3:
    lst=line.split(",")
    list_of_price.append(lst[1])
    list_of_intererst.append(lst[6])
del list_of_price[0:6]
del list_of_price[18:]
del list_of_intererst[0:6]
del list_of_intererst[18:]
list_of_price=list(map(float,list_of_price))
list_of_intererst = list(map(float,list_of_intererst))
print(list_of_price)
print(list_of_intererst)
max_interest = max(list_of_intererst)
# print(max(list_of_price))
mean_SP = sum(list_of_price)/(len(list_of_price))
print("mean of prices",mean_SP)
print("Maximum of the interest",max_interest)
fil3.close()


#____________________________week 5_____________________________

def last_four(x):
    s = str(x)
    return int(s[-4:])
ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_ids = sorted(ids,key=last_four)
print(sorted_ids)

sorted_id =sorted(ids,key=lambda x:str(x)[-4:])
print(sorted_id)

ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
lambda_sort =sorted(ex_lst,key=lambda x:x[1])
print(lambda_sort)
