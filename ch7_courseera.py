#chapter 7(I)
fname = input("Enter file name: ")
f = open(fname)
for line in f:
    b=line.rstrip()
    c=b.upper()
    print(c)
f.close()

#chapter 7 (II)
avg = 0
count = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        count += 1
        str = line[line.find(" "):len(line)-1]
        num = float(str)
        avg = avg+num
    else:
        continue

print("Average spam confidence:",avg/count)   

#chapter 8(I)
fname = input("Enter file name: ")
b=list()
f= open(fname)
for line in f:
    line = line.rstrip('\n')
    a = line.split(" ")
    for words in a:
        if words not in b:
            b.append(words)
            continue
        else :
            continue
b.sort()
print(b)

#chapter 8(II)
fname = input("Enter file name: ")
f= open(fname)
count =0
for line in f:
    if line.startswith("From "):
        count += 1
        line =line.rstrip("\n")
        lst = line.split(" ")
        mail = lst[1]
        print(mail)
print("There were", count, "lines in the file with From as the first word")
f.close()


#chapter 9
dic = dict()
mail_list = list()
fname = input("Enter file name: ")
f= open(fname)
for line in f:
    if line.startswith("From "):
        line = line.strip('\n')
        lst = line.split(" ")
        mail_list.append(lst[1])

for mail in mail_list:
    dic[mail]= dic.get(mail,0)+1

initial = 0
for key in dic:
    if dic[key] > initial:
        initial = dic[key]
for key in dic:
    if dic[key] == initial:
        print(key,initial)  


#chapter 10
fname = input("Enter file name: ")
f= open(fname)
hour_dict = dict()
hour_list = list()
for line in f:
    if line.startswith('From '):
        line = line.strip('\n')
        lst = line.split(" ")
        hour_list.append(lst[6].split(":")[0])

for hours in hour_list:
    hour_dict[hours] = hour_dict.get(hours,0)+1
  
b = sorted(hour_dict.items())
for k,v in b:
    print(k,v)

