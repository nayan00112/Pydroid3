# List in Python by Nayankumar 210160107048

# my_List = [3, 8, 1, 6, 0, 8, 4]

# 1. Make a list of the above integer numbers
my_List = [3, 8, 1, 6, 0, 8, 4]


# 2. Display all elements.
print("Our list is: ", end="")
print(my_List)

# 3. Perform the addition of all members of the list. (Using the direct function and without using the direct function)

# using function
print("sum of list elements is: ")
print("By direct function:")
print(sum(my_List))

#without function
print("Without direct function:")
s = 0
for i in my_List:
    s += i
print(s)

# 4. Print all elements in reverse. (Using the direct function and without using a direct function)

#using function
print('Reverse elements of list using direct function:')
my_List.reverse()
print(my_List)
my_List.reverse() #back to orignal

#without function
print('Reverse elements of list without using direct function:')
l = len(my_List)-1
while l > 0:
    print(my_List[l], end=" ")
    l -= 1

list2 = [42, 21, 45, 65, 49, 99, 26]
# 5. Remove a particular number from the list. (Example No: 45 – must be present in your list)
print("List before remove: ")
print(list2)
print("After removed: ")
list2.remove(45)
print(list2)

# 6. Write a Python program to get the largest number from a list.
print('Max number of list is: ', end="")
print(max(list2))

# 7. Write a Python program to remove duplicates from a list.
list3 = [54, 23, 21, 54, 65, 54, 23, 42, 28, 56]
tempSet=[]
print("Original List3 is: ")
print(list3)
list3 = [*set(list3)]
print("list after removing duplicates is: ") 
print(list3) 
     
# 8. Sort items in a list in ascending order. (Using the direct function and without using direct function)
print("Before sorting list is: ", list3)
print("Sort items in a list using direct function: ")
list3.sort()
print(list3)

list4 = [48, 32, 74, 24, 11, 93, 73]
print("Before sorting list is: ", list4)
print("Sort list items without direct functio (Bubble sort):")
j=0
for i in range(len(list4)):
    while ( j<len(list4)-i-1):
        if list4[j] > list4[j+1]:
            list4[j],list4[j+1]=list4[j+1],list4[j]
        j+=1
    j=0

print(list4)        

        