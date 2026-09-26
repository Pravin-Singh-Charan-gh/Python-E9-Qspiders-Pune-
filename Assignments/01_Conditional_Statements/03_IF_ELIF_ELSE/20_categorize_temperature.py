# 20.	Categorize temperature (freezing, cold, warm, hot, extreme).

temp = float(input('Enter Temperature : '))

if temp<=0:
    print('Freezing')
elif temp<=15:
    print('Cold')
elif temp<=30:
    print('Warm')
elif temp<=40:
    print('Hot')
else:
    print('Extreme')