# Bubble Sort
# 16/08/2023

a=[3,5,2,7,8,1]

l=len(a)

for i in range(l-1):
    for j in range(l-i-1):
        print(a)
        if a[j]>a[j+1]:
            t=a[j+1]
            a[j+1]=a[j]
            a[j]=t 
            print('replace', a)
    print()            
print(a)            