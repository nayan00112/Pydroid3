# Library Book Search: Design an algorithm that allows users to search for books in a library by title, author, or genre.


books={
    'Art Of living': ('art of living', 'shruti', 2),
    'gourgious maths' : ('gourgious maths', 'deepak', '1'),
    'wonder physics' : ('wonder physics', 'alakh panday', '1')
    }


print('1. title\n2. author\n3. generetion')
n = int(input('Enter choice: '))
n-=1
b=input('Enter keywords: ')
for i in books:
    if b == str(books[i][n]):
        print(books[i])
  