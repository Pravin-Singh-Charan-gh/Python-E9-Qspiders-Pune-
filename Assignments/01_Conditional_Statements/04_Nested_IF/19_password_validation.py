##19.	Multi-level password validation (length → digit → special char).

s = input('Enter the password : ')

if len(s)>=8:
    if '0' in s or '1' in s or '2' in s or '3' in s or '4' in s or '5' in s or '6' in s or '7' in s or '8' in s or '9' in s:
        if '!' in s or '@' in s or '#' in s or '$' in s or '%' in s or '^' in s or '&' in s or '*' in s or '(' in s or ')' in s:
            print('Valid Password')
        else:
            print('Special Character is not present')
    else:
        print('NO digit present')
else:
    print('Password length should be greater than 8')