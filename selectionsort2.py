#Selection sort:
 
a=[8,5,4,1,3, 4, 59, 284, 39, 394, 2]

l=len(a) #5

i=0

while i<l-1: #4 times
    j=i
    print(a)
    while j<l:
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
        j+=1
    i+=1
    
print(a)                      