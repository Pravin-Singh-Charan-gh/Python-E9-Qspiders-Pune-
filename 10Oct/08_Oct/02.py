#WAP to check whether the number is prime or not using recursion

def is_prime(n,i=2):
    if i==n:
        return True
    elif n%i==0:
        return False
    return is_prime(n,i+1)

print(is_prime(2))
