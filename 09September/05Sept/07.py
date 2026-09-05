db = {
      'qspiders':'wakad@123',
      'pravin':'pravin@123'
    }

un = input('Enter the username : ')
pwd = input('Enter the password : ')

while not db.get(un) or db[un]!=pwd:
    print('Wrong Credentials ')
    un= input('Enter the username : ')
    pwd = input('Enter the password : ')

print('Login Successful')