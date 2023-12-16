# Develop a program to understand the control structures of python.

# If else control structure:
a = 4
b = 5
if a>b:
    print("a is grater.")
else:
    print("b is grater.")

# if elif else control structure
binaryDigit=1
if binaryDigit == 1:
    print("True")
elif binaryDigit == 0:
    print("False")
else:
    print("Invalid binary digit.")
    
# loop
print("for loop")
for i in [1,2,3,4]:
    print(i)

for i in range(5):
    print(i**i) 

print("while loop")
i = 1
while i < 15:
    print(i)
    i+=3
