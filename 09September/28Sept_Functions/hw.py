#WAP to print first n perfect numbers

def is_prime(n):
    if n<=1:
        return False

    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True

n = int(input('Enter the number : '))
count = 0
p = 1
while count<n:
    q = 2**p-1
    if is_prime(q):
        print(q*(q+1)//2)
        count+=1
    p+=1