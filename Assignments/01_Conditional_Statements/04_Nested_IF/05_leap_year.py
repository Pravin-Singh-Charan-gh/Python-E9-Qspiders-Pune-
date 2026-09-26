##5.	Check if year divisible by 4 → then divisible by 100 → then 400.

year = int(input('Enter the year : '))

if not year%4:
    if year%100 or year%400==0:
        print('Leap Year')
    else:
        print('No Leap year')
        
else:
    print('No Leap year')
