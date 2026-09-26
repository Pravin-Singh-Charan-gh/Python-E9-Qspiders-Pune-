##7.	Identify day of week based on number (1–7).

days = ['Sun','Mon','Tues','Wednes','Thurs','Fri','Sat']

day = int(input('Enter the day : '))
if 1<=day<=7:
    print(str(days[day-1])+'day')
else:
    print('Invalid Day')
