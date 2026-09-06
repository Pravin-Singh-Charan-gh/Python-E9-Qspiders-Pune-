##14.	E-commerce discount:
##•	Cart > 1000 → 10%

amount = float(input('Enter the amount : '))

if amount>1000:
    print('TOTAL :',amount-amount*10/100,'Rs. (10% discount applied)')
else:
    print('TOTAL :',amount)