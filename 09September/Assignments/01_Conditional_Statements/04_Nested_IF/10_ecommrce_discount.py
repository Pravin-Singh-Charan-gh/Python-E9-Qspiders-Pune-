##10.	E-commerce discount system (cart amount → membership type).

amount = float(input('Enter the amount : '))
membership_type = input('Enter the membership type (gold, diamond or no membership): ').lower()

if membership_type=='gold':
    print('TOTAL : ',amount-amount*10/100)
elif membership_type=='diamond':
    print('TOTAL :',amount-amount*20/100)
else:
    print('TOTAL : ',amount)

