# Prime Number Checker: Create an algorithm that checks if a given number is prime using a loop to test divisibility.
import math as m
n = int(input('Enter number: '))
s = int(m.sqrt(n))
i=2
f=0
while i<s:
    if n%i==0:
        f=1
        break
    i+=1
    
if f==1:
    print('Non prime number')
else:
    print('Prime number')