
#identify the day of week based on number (1-7)

days = ['Sunday','Monday','Tuesday','Wedneday','Thursday','Friday','Saturday']

n = int(input('Enter day number : '))


if 1<=n<=7:
    print(days[n-1])
else:
    print('Invalid')
