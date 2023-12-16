# Number Comparisons: Create an algorithm that takes two numbers as input and outputs whether the first number is greater, smaller, or equal to the second number.

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

if num1>num2:
    print('First entered number is grater.')
    print(num1, end='')
    print('>', end='')
    print(num2, end='')
elif num1<num2:
    print('First entered number is smaller.')
    print(num1, end='')
    print('<',end='')
    print(num2, end='')
else:
    print('both are equal.')
    print(num1, end='')
    print('=', end='')
    print(num2, end='')