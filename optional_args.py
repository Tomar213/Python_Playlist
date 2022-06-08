def multiple_args(x,y=6,z=12):
    print('x,y,z are:',x,y,z)
multiple_args(100,z=200,y=300)

def mult(x,y=6):
    return x*y
print(mult("roman"))

def greeting(name,greeting="Hello ",  excl="!"):
    return greeting + name + excl

print(greeting("Bob"))
print(greeting(""))
print(greeting("Bob", excl="!!!"))


def checkingIfIn(x,bol=True,dict1={'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if bol ==True:
        if x in dict1.keys():
            return True
        else:
            return False
    elif bol ==False:
        if x not in dict1.keys():
            return True
        else :
            return False
print(checkingIfIn('apple',bol=False))




def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]

# Call the function so that it returns False and assign that function call to the variable c_false
c_false = checkingIfIn('pome')
print(c_false)
c_true = checkingIfIn('pome',direction=False)
print(c_true)
fruit_asn = checkingIfIn('apple')
print(fruit_asn)
# Call the function using the first and third parameter so that the value 8 is assigned to the variable param_check
param_check = checkingIfIn('watermelon')+1
print(param_check)
