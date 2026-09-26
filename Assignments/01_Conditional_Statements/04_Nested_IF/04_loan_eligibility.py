##4.	Bank loan eligibility (age check → income check).

age = int(input('Enter the age : '))
income = int(input('Enter the income : '))

if age>25:
    if income>500000:
        print('You are eligible for loan')
    else:
        print('Not eligible')
else:
    print('Not eligible')