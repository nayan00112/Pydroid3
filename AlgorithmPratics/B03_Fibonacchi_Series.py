# Fibonacci Sequence: Design an algorithm to generate the first n numbers in the Fibonacci sequence using a loop.

j = 0
k = 1
print(j)
print(k)
for i in range(50):
    print(j+k)
    t=j
    j=k
    k+=t
    
    