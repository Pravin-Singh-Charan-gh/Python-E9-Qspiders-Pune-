# 14. Print all prime numbers between 1 and 100.

def is_prime(n,primes):
    if n==1:
        return False
    for i in primes:
        if n%i==0:
            return False
    return True

primes = []
for i in range(1,101):
    if is_prime(i,primes):
        primes.append(i)

print(primes)