# Ticket pricing (weekday price, weekend price, senior discount).

# Ticket Pricing
weekday_price = 20
weekend_price = 25
senior_discount = 0.20

day = input('Enter day : ').lower()
age = int(input('Enter the age : '))

weekdays = ['monday','tuesday','wednesday','thurday','friday']
weekends = ['saturday','sunday']

bill = 0
if day in weekdays:
    bill+= weekday_price
elif day in weekends:
    bill+=weekend_price
else:
    print('Invalid day type')
    exit()

if age>=60:
    bill= bill - bill*senior_discount

print('Final Ticket Price : ',bill, ' Rs.')
