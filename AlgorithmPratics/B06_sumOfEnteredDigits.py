# Sum of Digits: Design an algorithm to calculate the sum of digits of a given number using a loop.

n=int(input('Enter number: '))
s=0
while n > 0:
    s=s+(n%10)
    n=int(n/10)
    
print(s)