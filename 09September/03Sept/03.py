#check if the date is valid or not(day-month-year)

day = int(input('Enter date : '))
month = int(input('Enter month : '))
year = int(input('Enter year : '))

if month>12 or month<1 or day<0 :
    print('Invalid')

elif month==2:

elif month in (1,3,5,7,8,10,12):
    