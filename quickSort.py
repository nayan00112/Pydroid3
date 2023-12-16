a = [38,46,41,9,8]
a.append(99)

l= 0
h= len(a)-1

def qsort(a, l, h):
    if l<h:
        j=partition(a, l, h)
        qsort(a, l, j)
        qsort(a,j+1, h)
    
def partition(a, l, h):
    p=a[l]
    i=l
    j=h
    while i<j:
        while a[i]<=p:
            i+=1
        while a[j]>p:
            j-=1
        if i<j:
            a[i],a[j]=a[j],a[i]
    a[l],a[j]=a[j],a[l]
    return j   
qsort(a, l, h)
print(a)
