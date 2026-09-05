# Check if a year is leap year (proper logic).

year = int(input('Enter the year : '))

if (year%4==0 and year%100) or year%400==0:
    print(year,' is a leap year')
else:
    print(year,' is a not leap year')
