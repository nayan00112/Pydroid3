# GCD and LCM Calculator: Write an algorithm to calculate the Greatest Common Divisor (GCD) and Least Common Multiple (LCM) of two numbers using loops.

def gcd(n1,n2):
    t4=0
    while True:
        t2=int(n1/n2)
        t3=(n1-(n2*t2))
        if(t3==0):
            return t4
        n1=n2*t2 + t3
        # print(n1,'=',n2,'*',t2,'+',t3)
        #print('%5d = %5d * %3d + %3d'%(n1,n2, t2, t3))
        n1=n2
        n2=t3
        t4=t3
        


n1=int(input('Enter fires number: '))

n2=int(input('Enter second number:'))

if n1>n2:
    pass
else:
    n1,n2=n2,n1

print(gcd(n1,n2))

