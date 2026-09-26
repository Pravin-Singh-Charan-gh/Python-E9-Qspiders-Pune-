##2.  Login system (check username → then password).

db = {
    'qspiders':'wakad@123',
    'Pravin':'Pravin@123'
}

un = input('Enter Username : ')
pwd = input('Enter Password : ')

if db.get(un):
    if db[un]==pwd:
        print('Logged In')
    else:
        print('Incorrect Password')
else:
    print('Username does not exist. Please signup')