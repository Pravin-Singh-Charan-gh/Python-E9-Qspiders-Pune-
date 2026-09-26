#WAP to check the first prime number between two number

n1 = int(input('Enter the first number : '))
n2 = int(input('Enter the second number : '))

for i in range(n1,n2+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
        break