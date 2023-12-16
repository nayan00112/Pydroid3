# Multiplication Table: Write an algorithm to generate the multiplication table of a given number using nested loops.

n = int(input('Enter Number: '))

for i in range(n):
    for k in range(n):
        print('%4d' %((i+1)*(k+1)), end=' ')
    print()