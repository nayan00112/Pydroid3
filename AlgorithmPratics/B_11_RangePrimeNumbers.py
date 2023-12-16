# prime number generater range.

import math

def isPrime(n):
    m= int(math.sqrt(n))
    if n==0 or n==1:
        return False
    i=2
    while i<=m:
        if n%i==0:
            return False
        i+=1
    return True
           

n1 = int(input('Enter Number: '))   
for i in range(n1): 
    if isPrime(i):
        print(i)      