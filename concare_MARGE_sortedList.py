a = [7, 8, 34, 99, 103]
b = [2, 4, 9, 10, 23, 44, 88, 89]

c = []
i = 0
j = 0
while (i<len(a) and j<len(b)):
    if a[i]<b[j]:
        c.append(a[i])
        i+=1
    if a[i]>=b[j]:
        c.append(b[j])
        j+=1
    print(c) 
    
print()  
 
while j<len(b):
    c.append(b[j])
    j+=1
    print(c)
    
print() 
while i<len(a):
    c.append(a[i])
    i+=1
    print(c)

print() 
print(c)