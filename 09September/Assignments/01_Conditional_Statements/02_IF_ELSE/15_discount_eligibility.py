#15.	Check if a person is eligible for discount (age < 18 or > 60 AND purchase > 500).

purchase = int(input('Enter the amount : '))
age = int(input('Enter the age : '))

if (0<=age<18 or age>60) and purchase>500:
    print('Yes')
else:
    print('No')