# 13.	ATM withdraw system (invalid amount, insufficient balance, successful).

Balance = 100000
amount = int(input('Enter the amount to withdraw : '))

if amount<=0:
    print('INVALID AMOUNT')
elif amount>Balance:
    print('INSUFFICIENT BALANCE')
    print('Available balance : ',Balance)
else :
    Balance -= amount
    print(f'{amount} Rs. WITHDRAWN SUCCESSFULLY')
    print('Available balance : ',Balance)