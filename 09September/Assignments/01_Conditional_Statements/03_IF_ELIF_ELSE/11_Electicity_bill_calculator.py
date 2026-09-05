##11.	Mini electricity bill calculator (different rates for 0–100, 101–300, 300+ units).

units = int(input('Enter units of electricity : '))

if units<0:
    print('Invalid units')
elif units<=100:
    print(f'Bill : {units*3} Rs.')
elif units<=300:
    print(f'Bill : {100*3 + (units-100)*5} Rs.')
else:
    print(f'Bill : {100*3 + 200*5 + (units-300)*7} Rs.')
    