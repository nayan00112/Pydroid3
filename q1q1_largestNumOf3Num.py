# Find the largest number from 3 numbers and print on the screen.
# By Nayankumar (210160107048)

# take number from user and assign to variable
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
z = int(input('Enter third number: '))

# largest number
print("Largest number is: ", end='')
if x > y:
    if x > z:
        print(x)
    else:
        print(z)
else:
    if y > z:
        print(y)
    else:
        print(z)
