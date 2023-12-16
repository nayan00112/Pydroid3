# Leap Year Checker: Design an algorithm that checks if a given year is a leap year (divisible by 4, but not divisible by 100 unless also divisible by 400).

year=int(input('Enter year:'))

if (year%4==0 and year%100!=0) or year%400==0:
    print('leap year')
else:
    print('Not leap year')
    
# new for me this condition. help from chatGPT.