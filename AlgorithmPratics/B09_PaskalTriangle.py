# Print Pascal's Triangle: Design an algorithm to print Pascal's Triangle for a given number of rows using nested loops.

def fact(n):
    r=1
    while n!=0:
        r=r*n
        n-=1
    return int(r)

def combination(n,r):
    t1=fact(n)
    r2=fact(r)
    return int((t1/(fact(n-r)*r2)))

t=int(input('Enter number: '))

for i in range(t):
    for k in range(t-i):
        print('   ',end='')
    for j in range(i+1):        
        print('%3d  ' %combination(i,j), end=' ')
    print()