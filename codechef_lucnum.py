T = int(input("Number of test cases:"))
for i in range(T):
    N= int(input("Enter the number:"))
    while True:
        if N%2==0:
            print("2*")
            N=N%2
        else:
            print(int(N/2))
            break

