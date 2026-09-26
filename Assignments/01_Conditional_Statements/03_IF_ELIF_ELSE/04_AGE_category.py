##4.	Categorize age (child, teen, adult, senior).

age = int(input('Enter the age : '))

if age<0:
    print('Invalid Age')
elif age<=12:
    print('Child')
elif age<=18:
    print('Teenager')
elif age<=59:
    print('Adult')
else:
    print('Senior')