##18.	Car insurance eligibility (age + accident history).

age = int(input('Enter the age : '))
accidents = int(input('Enter the number of accidents : '))

if age>=18:
    if accidents<=2:
        print('Insurance Eligible')
    else:
        print('Not eligible')
else:
    print('Not eligible')
        