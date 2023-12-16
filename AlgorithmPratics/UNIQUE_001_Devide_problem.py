a=[4,5,9,6,7,9,12, 57,466,35,32,57,32,47,48,32,13,45]


def sp(a, x, y):
    x=int(x)
    y=int(y)
    print(a[x:y])
    #print(x,y)
    if y-x>1:
        mid = (x + y)/2       
        sp(a,x, mid)
        sp(a,mid,y)
    #elif y-x==1:
        #print(a[x])        
    else:
        pass
   
    
sp(a, 0, len(a))
  