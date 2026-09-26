#WAP To check whether the number is prime number or not

n = int(input('Enter the number : '))

is_prime = True
for i in range(2,n):
    if n%i==0:
        is_prime = False

if is_prime and n!=1:
    print('Prime')
else:
    print('Not Prime')
