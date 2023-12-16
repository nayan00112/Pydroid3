a=[2,5,8,9,10,49,60,70,79,90]

print(a)
s = int(input('enter number: '))

def binsearch(a,l,h,s):
    while l<=h:
        mid=int((l+h)/2)
        if a[mid]==s:
            return mid
        if a[mid]>s:
            h=mid-1
        else:
            l=mid+1
    return "Not Found"
        
r=binsearch(a,0,len(a)-1,s)    
print(r) 

    