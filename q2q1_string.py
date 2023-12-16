# 1) Understand various inbuilt python functions for text manipulation.
#By Nayankumar(210160107048)
a = "Hello, World! "
age = 36
txt = "My name is John, and I am"

# 1. Print value of a.
print(a)

# 2. Print first character
print(a[0])

# 3. Print 2nd to 5th character.
print(a[2:5])

# 4. Remove extra space at last.
print(a[:-1])

# 5. Find the length of a string.
print(len(a))

# 6. Convert all letters into lowercase.
print(a.lower())

# 7. Convert all letters into upper case.
print(a.upper())

# 8. Using age and text, display “My name is John, and I am 36 years old.”
print(txt, str(age) + " years old")
