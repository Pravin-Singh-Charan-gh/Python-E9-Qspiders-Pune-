##20.	Check if a date is valid (day-month-year basic check).

day = int(input('Enter the day : '))
month = int(input('Enter the month : '))
year = int(input('Enter the year : '))

if month in (1,3,5,7,8,10,12):
    if 1<=day<=31:
        print('Valid')
    else:
        print('Not Valid')

elif month in (4,6,9,11):
    if 1<=day<=30:
        print('Valid')
    else:
        print('Invalid')

elif month==2:
    if (year%4==0 and year%100) or year%400==0:
        if 1<=day<=29:
            print('Valid')
        else:
            print('Invalid')
    else:
        if 1<=day<=28:
            print('Valid')
        else:
            print('Invalid')