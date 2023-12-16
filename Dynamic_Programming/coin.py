d=[2, 4, 5]
N=7

c= [[0-1]*len(d) for _ in range(N)]
print(c)
for i in range(1, len(d)+1):
    for j in range(N):
        if i==1 and j<d[i]:
            c[i][j]=0-1
        elif i==1:
            c[i][j]=1+c[1][j-d[i]]
        elif j<d[i]:
            c[i][j] = c[i-1][j] 
        else:
            c[i][j]= min(c[i-1][j],1+c[1][j-d[i]])
                     
for i in c:
    print(i)         