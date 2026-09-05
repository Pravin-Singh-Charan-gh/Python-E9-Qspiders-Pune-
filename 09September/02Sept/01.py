database = {'qspider':'wakad@123',
            'asp':'anurag@123'}

un= input('Enter username : ')
pwd = input('Enter password : ')

if database.get(un):
    if database[un]==pwd:
        print('Login Successful')
    else:
        print('Wrong Password')

else:
    print('Username not exist')
