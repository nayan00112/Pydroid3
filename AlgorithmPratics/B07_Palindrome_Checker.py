# Palindrome Checker: Create an algorithm that checks if a given word or number is a palindrome (reads the same forwards and backwards) using loops.

i=input('Enter string (include case sensitiveness): ')
r=len(i)
f=0
for j in range(int(r/2)):
    if i[j]==i[r-j-1]:
        pass
    else:
        f=1
        break
if f==0:
    print('Palindrone')
else:
    print('Not Palindrome.')