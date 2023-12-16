import math as Maths

def fun(y):
    # y = (1/15) * (x - 25)^2
    x1=int(Maths.sqrt(15*y)+25)
    x2=int(25-(Maths.sqrt(15*y)))
    
    return x1,x2

rangeNum=60
space=5

for y in reversed(range(rangeNum)):
    x1,x2=fun(y)
    for t in range(space):
        print(' ', end='')
    for x in range(rangeNum):
        if x1==x or x2==x:
            print("*", end='')
        else:
            print(" ", end="")
    print()