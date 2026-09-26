#WAP to print all the devisors of the given number

n = int(input('Enter the number : '))

for i in range(1,n):
    if n%i==0:
        print(i)