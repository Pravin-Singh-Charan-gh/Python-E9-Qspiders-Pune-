##8.	Student scholarship (marks → family income).

marks = int(input("Enter Student's marks : "))
income = int(input('Enter income : '))

if marks>=80:
    if income<400000:
        print("Eligible for scholarship")
    else:
        print('Not eligible')
else:
    print('Not eligible')