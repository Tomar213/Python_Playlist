#vid = 39

import random           #this is a built-in module to generate a random number 

random_no = random.randint(1,20)       #generate any random integer b/w 1 and 20
print(random_no)

rand = random.random()               #random decimal number generation
print(rand)
rand2 = random.random()*100           #random number in 100s
print(rand2)


lst = ["harry ","karan","grammer ","Hoshiyar"]
ran = random.choice(lst)
print(ran)

