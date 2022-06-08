#by recursive approach
                                    #Global variable
def factorial_rec(n):
    if(n==1):
        return 1
    else:
        return  n* factorial_rec(n-1)

# by itertive approach
def factorial_ittrative(n):
    fact =1 
    for  i in range(n):
        fact = fact * (i+1)
    return fact 
n = int(input("ENTER A NUMBER : "))
print("factorial by the recursive approach is : ",factorial_rec(n))     
print("factorial by the recursive approach is : ",factorial_ittrative(n))     


#fibonacci series 
def fibonacci(m):
    if(m==1):
        return 0
    elif (m==2):
        return 1
    else:
        return  fibonacci(m-1)+fibonacci(m-2)        
m = int(input("ENTER A NUMBER : "))    
print("fibonacci = ",fibonacci(m))   