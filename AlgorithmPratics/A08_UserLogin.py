# Login System: Design an algorithm that prompts the user for a username and password. If the input matches predefined values, output a successful login message; otherwise, indicate a failed login attempt.

db={
'nayan':'nayan12345',
'marmik':'marmik12345',
'jignesh':'jignesh1',
'rudra':'rudra09'
}

u = input('Enter username: ')
p = input('Enter password: ')

if db.get(u)==p:
    print('welcome, you are loged in!')
else:
    print('wrong username of password.')