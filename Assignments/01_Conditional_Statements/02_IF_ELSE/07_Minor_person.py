##7.	Check if a person is minor or adult.

age = int(input('Enter the age : '))

if 0<=age<18:
    print('Minor')
elif age>=18:
    print('Adult')
else:
    print('Invalid Age')