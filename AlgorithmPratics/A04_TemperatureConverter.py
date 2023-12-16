# Temperature Converter: Write an algorithm that converts temperatures between Celsius and Fahrenheit based on user input.
def ftoc():
    f=int(input('Enter temperature in C: '))
    return (f-32)*5/9
def ctof():
    c=int(input("Enter temperarure in F: "))
    return 1.8*c+32

print('1. Fahrenheit to Celsius')
print('2. Celsius to Fahrenheit')
x=int(input('Enter Choice: '))
if x==1:
    print('Celsius:', round(ftoc(),3))
elif x==2:
    print('Fahrenheit:',round(ctof(),3))
else:
    print('Invalid inpit.')