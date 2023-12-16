#i=int(input('enter '))
i=6
j=1
while j <= i:
    k=i-j
    while k>0:
        print(' ', end='')
        k-=1
    t=j
    while t>0:
        print('* ', end="")
        t-=1
    j+=1
    print() 
m=1    
while m<i:
    n=1
    while n<m:
        print(' ', end='')
        n+=1
    l=i-m
    while l>0:
        print(' *', end='')
        l-=1
    m+=1
    print()