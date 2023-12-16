# selection sort

a=[3,9,2,7,1]
l=len(a)
print(a)
for i in range(l-1):
    for k in range(l-i):
         if a[i]>a[k+i]:
             a[i],a[k+i]=a[k+i],a[i]
    print(a)   
print('sorted array: ')
print(a)         