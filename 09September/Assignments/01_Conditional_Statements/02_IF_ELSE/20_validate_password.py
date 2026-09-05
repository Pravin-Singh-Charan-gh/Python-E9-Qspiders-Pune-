##20.	Validate password: length ≥ 8 AND contains digit.

password = input('Enter the password : ')

if len(password)>=8 and password.isdigit():
    print('YES')
else:
    print('No')