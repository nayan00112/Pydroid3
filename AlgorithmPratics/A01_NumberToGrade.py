# Grade Classifier: Write an algorithm that takes a student's score as input and outputs their corresponding grade (A, B, C, etc.) based on a predefined grading scale.
tmarks=int(input('Total marks: '))
amarks=int(input('Achived marks: '))

per=float(amarks)*100/float(tmarks)
print('Percentage is:', str(round(per,2)) + '%')
print('Class: ', end="")
if per>95:
    print("A+")
elif per>90:
    print("A")
elif per>85:
    print("B+")
elif per>70:
    print("B")
elif per>60:
    print("C")
elif per>40:
    print('D')
elif per>34:
    print('E')
elif per>0:
    print('F')
else:
    print('invalid')