#Counting Characters: Create an algorithm that counts the occurrences of a specific character in a given string using a loop.   

s=input('Enter string: ')
c=input('Enter character: ')
count=0
for i in s:
    if c[0]==i:
        count+=1
   
print('Ocurrences is:', count)