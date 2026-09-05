##12.	Loan approval:
##•	Age ≥ 21
##•	Salary ≥ 25k
##•	If salary < 40k → need guarantor

age = int(input('Enter the age : '))
salary = int(input('Enter the salary : '))

if age>=21:
    if salary>=40000:
        print('You are eligible')
    elif salary>=25000:
        print('You are eligible but need guarantor')
    else:
        print('Not eligible')
else:
        print('Not eligible')