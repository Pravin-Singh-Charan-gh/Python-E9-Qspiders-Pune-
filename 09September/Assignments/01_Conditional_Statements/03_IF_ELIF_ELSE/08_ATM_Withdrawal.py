##8.	ATM withdrawal check (balance > amount, insufficient, zero balance).

Balance = 100000

amount = int(input('Enter the amount to withdraw : '))

if amount>Balance : 
    print('Insuffcient Balance')
    print('Balance :',Balance)
elif  Balance==0:
    print('0 Balance')
else:
    Balance-=amount
    print(amount,'Rs. Withdrawn successfully')
    print('Balance :',Balance)