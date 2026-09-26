##9.	ATM system (loop until user exits).

balance = 100000

option = 1

while option:
    match option:
        case 1:
            print(f"Balance : {balance} Rs." )
        case 2:
            amount = int(input('Enter amount to withdraw : '))
            if amount>balance:
                print(f'Insuffient Balance : {balance} Rs.')
            else:
                balance-=amount
                print('Amount Withdrawn Successfully')
                print(f"Balance : {balance} Rs." )
        case 3:
            amount = int(input('Enter amount to credit : '))
            balance+=amount
            print('Amount Credited Successfully')
            print(f"Balance : {balance} Rs." )
        case _ :
            print('Invalid Input')

    print('\n=================================\n')

    print('Choose Option :')
    print('1. To check account balace')
    print('2. To withdraw from account')
    print('3. To credit to account')
    print('0. To exit')
    option = int(input('Choose the option : '))

print('Bye')