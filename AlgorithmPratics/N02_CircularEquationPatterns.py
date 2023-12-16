# circular fill pattern 
import math as Maths

#radious
r=4

h=8
g=8


# circle
def func(x,y):
    return (round((x-h)**2 +(y-g)**2 )<= r**2)    
        
        
for y in range(15,0,-1):
    for x in range(20):
        if func(x,y):
            print("* ", end="")
        else:
            print('  ', end='')
    print()