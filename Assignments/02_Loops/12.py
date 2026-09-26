##12.	Keep asking user until valid email format entered.

is_valid = False

while not is_valid:
    email = input('Enter the email : ')
    if len(email)<12:
        print('Size should be greater than 12')
    elif '@' not in email:
        print('Email must contain @ symbol')
    elif '.' not in email:
        print("Email must contain '.' symbol")
    else:
        is_valid=True

print('Email Format is valid')