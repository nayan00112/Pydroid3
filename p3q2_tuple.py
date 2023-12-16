my_Tuple = (3, 8, 1, 6, 0, 8, 4)
#1. Print all elements of the tuple.
print(my_Tuple)

#2. Write a Python program to find the length of a tuple.
print("Tuple length is:", len(my_Tuple))

#3. Write a Python program to check whether an element exists within a tuple.
n=int(input("Enter an element: "))
if n in my_Tuple:
    print('Exist')
else:
    print("Doesn't exist")
    
#4. Write a Python program to remove an item from a tuple.
print('As tuple in python is immutable, hence we cannot add or remove elements from it.')

#5. Write a Python program to find the index of an item of a tuple.
i=int(input("Enter an element: "))
if i in my_Tuple:
    print(my_Tuple.index(i))
else:
    print("Doesn't exist")

#6. Write a Python program to find the repeated items of a tuple.
s={}
for i in my_Tuple:
    for j in my_Tuple:
        if i==j and my_Tuple.index(i)!=my_Tuple.index(j):
            s.add(i)
print('repeted element in tuple is: ')  
print(s)          