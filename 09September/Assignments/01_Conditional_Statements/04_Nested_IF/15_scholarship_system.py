##15.	Scholarship system:
##•	Marks ≥ 85
##•	Family income < 5 lakh
##•	If marks ≥ 95 → bonus stipend

marks = int(input('Enter the marks : '))
income = int(input('Enter income : '))

if 0<=income<500000 and 0<=marks<=100:
    if marks>=95:
        print('You are eligible for scholarship and bonus stipend')
    elif marks>=85:
        print('You are eligible for scholarship')
    else:
        print('You are not eligible')
else:
    print('You are not eligible')