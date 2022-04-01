
def ran():
    import random
    lst = ["S","W","G"]
    h=random.choice(lst)
    return h

print("\t\tSNAKE, WATER AND GUN GAME ")
print("S For Snake \nW For Water \nG for Gun\n")
u_count = 0
c_count = 0
count =0
draw =0
while count <10                                                                                                                                                          :
    a=str(ran())
    count = count +1
    # print(f"{count}  {a}")

    m= str(input("Pick one (S,W,G) : "))
    if(a=="G"and m=="W"):
        u_count = u_count+1
        print("you won")
    elif(a=="W"and m=="W"):
        draw = draw + 1 
        print("tie") 
    elif(a=="S"and m=="W"):
        c_count = c_count +1
        print("computer won")
    elif(a=="G" and
     m =="S"):
        c_count = c_count+1
        print("computer won")
    elif(a=="W" and m=="S"):
        u_count = u_count+1
        print("you won")
    elif(a=="S" and m=="S"):
        draw = draw + 1 
        print("tie") 
    elif(a=="G" and m =="G"):
        u_count = u_count+1
        print("you won")
    elif(a=="W" and m=="G"):
        draw = draw + 1 
        print("tie") 
    elif(a=="S" and m=="G"):
        u_count = u_count +1     
        print("you won")                

print(f"Your score = {u_count} \nOpponent score = {c_count} \nDraw = {draw}")     
if(u_count>c_count):
    print("You Are The Winner ")
elif(u_count<c_count):
    print("Computer Won The Game")   
else:
    print("GAME TIE")   
   