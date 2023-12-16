# traingle pattern by linear equatation
r=20
for y in reversed(range(r)):
    for x in range(r):
        if x>y:
            print('* ', end='')
        else:
            print(' ', end='')
    print()