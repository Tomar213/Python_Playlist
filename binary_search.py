# linear search.......................
lst = [12,43,56,45,23]
flag = 1
for item in lst:
    if item==56:
        print(f"56 is at {flag} position")
    flag += 1

# binary search..................
lst1 = [90,25,100,200,300,12,34,45,56,89]
lst1.sort()
print("YOUR LIST : ",lst1)
find = int(input("Enter the number to be found: "))
lb  = 0
ub =len(lst1)
mid_ele= 0
while True:
    mid = int((ub+lb)/2)
    if lst1[mid]==find:
        print(f"{find} is at position {mid+1}")
        break
    elif find > lst1[mid]:
        lb=mid
    elif find <lst1[mid]:
        ub = mid
    else:
        print(f"{find} is not not in the list.")


#BUBBLE SORT............
lst1 = [90,25,2,200,300,12,34,45,56,1]
print("List initially: ",lst1)
i=0
n= len(lst1)
iter =0 
for iter in range(len(lst1)-1):
    for i in range((len(lst1)-1)) :
        if lst1[i]==lst1[len(lst1)-1]:
            break
        elif lst1[i]>lst1[i+1]:
            temp = lst1[i]
            lst1[i]=lst1[i+1]
            lst1[i+1]=temp
        elif lst1[i]<=lst1[i+1]:
            continue
        i=i+1
    n=n+1
print("Final result: ",lst1)


#selection sort...........
def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = [-2, 45, 0, 11, -9]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)

    

