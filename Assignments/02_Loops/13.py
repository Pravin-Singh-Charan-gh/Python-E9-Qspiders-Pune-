##13.	Create simple number guessing game with limited attempts.


my_num = 85

n = int(input('Enter the number : '))
attempts = 1
while n!=my_num and attempts<=10:
    if n>my_num:
        print('Enter lesser number')
    else:
        print('Enter higher number')
        
    attempts +=1
    print('=================================')

    n = int(input('Enter the number : '))

if attempts>10:
    print('All attempts exhausted')
else:
    print('Number Matched')
