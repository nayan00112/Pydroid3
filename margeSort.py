arr= [4,1,6,9,2]
len= len(arr)

def margesort(a, l, h):
    if (l<h):
        mid=int((l+h)/2)
        margesort(a, l, mid)
        margesort(a, mid+1, h)
        marge(a, l, mid, h)

def marge(a, l, mid, h):
    l1= h - l + 1
    left=l
    right=mid+1
    c=[]
    
    while (left<=mid and right<=h):
        if a[left]<a[right]:
            c.append(a[left])
            left+=1
        else:
            c.append(a[right])
            right+=1
    while right<=h:
        c.append(a[right])
        right+=1     
    while left<=mid:
        c.append(a[left])
        left+=1
    for i in range(l1):
        a[l+i] = c[i]
    
margesort(arr,0,len-1)
print(arr)