#Write a program that takes a year as input and determines if it is a leap year.

def is_leap_year(year):
    if (year%4==0 and year%100!=0) or year%400==0:
        return True
    return False

year = int(input('Enter the number : '))
if is_leap_year(year):
    print('Leap Year')
else:
    print('Not a leap year')
