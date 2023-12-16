import math as Maths
def isPrime(n):
    m=int(Maths.sqrt(n))+1
    i=2
    while i<=m:
        if n%i == 0:
            return False
        i+=1
    return True
# prime or no-nprime numbers in range 20.
for j in range(2000):
    if isPrime(j):
        print(str(j) + ' is prime')
    else:
        print(str(j) + ' is non-prime')
