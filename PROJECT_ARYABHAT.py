#FIRST TRIAL TO PROJECT ARYABHAT
print("\t\t\tHELLO WELCOME TO OUR PROJECT ARYABHATA\n\t\t\t\t  IT'S A BETA TEST")
name=input("\n\nENTER YOUR NAME: ")
print(f"\nHELLO {name} TELL US WHAT YOU WANT TO DO")
print("\n1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.FACTORIAL\n6.SQUARE ROOT\n7.CUBE ROOT\n8.CHANGE RADIAN TO DEGREE\n9.CHANGE DEGREE TO RADIAN")
number=int(input("\nTELL US: "))
if number == 1:
      num1=int(input("ENTER FIRST NUMBER: "))
      num2=int(input("ENTER SECOND NUMBER: "))
      num3=(num1)+(num2)
      print(f"{num1}+{num2}= {num3}")
elif number == 2:
      num1=int(input("ENTER FIRST NUMBER: "))
      num2=int(input("ENTER SECOND NUMBER: "))
      num3=(num1)-(num2)
      print(f"{num1}-{num2}= {num3}")
elif number == 3:
      num1=int(input("ENTER FIRST NUMBER: "))
      num2=int(input("ENTER SECOND NUMBER: "))
      num3=(num1)*(num2)
      print(f"{num1}x{num2}= {num3}")
elif number == 4:
      num1=int(input("ENTER FIRST NUMBER: "))
      num2=int(input("ENTER SECOND NUMBER: "))
      num3=(num1)/(num2)
      print(f"{num1}/{num2}= {num3}")
elif number == 5:
      n=int(input("ENTER THE NUMBER TO FIND FACTORIAL: "))
      result = 1
      for i in range(1,n+1):
         result = result*i
      print("THE FACTORIAL OF",n,"IS",result)
elif number == 6:
      sqr=int(input("ENTER THE NUMBER TO FIND THE SQUARE ROOT: "))
      ans=(sqr**(1/2))
      print("SQUARE ROOT OF",sqr,"IS",ans)
elif number ==7:
      sqr=int(input("ENTER THE NUMBER TO FIND THE SQUARE ROOT: "))
      ans=(sqr**(1/3))
      print("CUBE ROOT OF",sqr,"IS",ans)
elif number==8:
      rad=int(input("ENTER YOUR RADIAN VALUE: "))
      deg=int
      deg=(rad)*(57.29)
      print(rad,"RADIAN IS",deg,"DEGREE")
elif number==9:
      deg=float(input("ENTER YOUR DEGREE VALUE: "))
      rad=int
      rad=(deg)/(57.29)
      print(deg,"DEGREE IS",rad,"RADIAN")
else:
      print("\nPLEASE CHOOSE VALID PROGRAM NUMBER:")
input("\nENTER ANY KEY TO EXIT THE PROGRAM :>")
