# Print Patterns: Create an algorithm that prints various patterns of asterisks, numbers, or other characters using nested loops.

for i in range(5):
    for j in range(5-i+1):
        print(' ', end='')
    for j in range(1+i):
        print('* ',end='')
    print()
    
    
    
for i in range(5):
    for k in range(5-i+1):
        print('  ',end='')
    for k in range(1+i):
        print('* ', end='')
    print()
    
 
for i in range(5):
    for k in range(i+1):
        print('* ', end='')  
    print() 
  
  
print()  
for i in range(5):
    for k in range(i):
        print(' ', end='')
    for k in range(5-i):
        print('* ', end='')
    print()
    
