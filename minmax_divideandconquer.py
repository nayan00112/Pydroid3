# MAX_MIN PROBLEM USIMG DIVIDE AND CONQUER ALGORITHM

a=[2,4,9,6,92,64]

def maxmin(a, l, h):
    if (l==h):
        return a[l],a[h]
    elif (h-l==1):
        if(a[l]>a[h]):
            max=a[l]
            min=a[h]
        else:
            max=a[h]
            min=a[l]
        return max,min
    else:
        mid=int((h+l)/2)
        mxl,mil=maxmin(a, l, mid)
        mxr,mir=maxmin(a,mid+1,h) 
        if mxl>mxr:
            max=mxl
        else:
            max=mxr
        if mil<mir:
            min=mil
        else:
            min=mir
        return max,min
        
max,min=maxmin(a, 0, len(a)-1)      
print(max,min)   


     