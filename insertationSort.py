#Insertion sort


a=[4,2,9,1,6,7]

n=len(a)
i=1

while i <= (n-1):
    t=a[i]
    j=i-1
    while j>=0 and a[j]>t:
        a[j+1]=a[j]
        j=j-1
    a[j+1]=t
    i+=1
    
print(a)