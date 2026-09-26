##17.	Check if a year is leap year using full correct rule (divisible by 4, not 100 unless also 400).

year = int(input('Enter the year : '))

if (year%4==0 and year%100!=0) or year%400==0:
    print('Yes')
else:
    print('No')