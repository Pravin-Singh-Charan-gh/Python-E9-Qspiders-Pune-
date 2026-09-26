##10.	Guessing game (loop until correct guess).

my_num = 85

n = int(input('Enter the number : '))

while n!=my_num:
    if n>my_num:
        print('Enter lesser number')
    else:
        print('Enter higher number')
    print('=================================')

    n = int(input('Enter the number : '))

print('Number Matched')
