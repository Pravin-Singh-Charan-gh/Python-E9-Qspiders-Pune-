##11.	Login system with 3 attempts only.

db = {
    'qspiders':'wakad@123',
    'Pravin':'Pravin@123'
}

un = input('Enter Username : ')
pwd = input('Enter Password : ')

if db.get(un) and db[un]==pwd:
    print('Login Successful')
else:
    print('Credentials not matched. 2 attempts remaining')
    un = input('Enter Username : ')
    pwd = input('Enter Password : ')

    if db.get(un) and db[un]==pwd:
        print('Login Successful')
    else:
        print('Credentials not matched. 2 attempts remaining')
        un = input('Enter Username : ')
        pwd = input('Enter Password : ')
    
        if db.get(un) and db[un]==pwd:
            print('Login Successful')
        else:
            print('Credentials not matched. All attempts exahusted')