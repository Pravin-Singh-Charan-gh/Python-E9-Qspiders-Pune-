##17.	Count number of prime digits in a number.

n = int(input('Enter the number : '))

primes = [2,3,5,7]
ans = 0

t = n
while t:
    rem = t%10
    if rem in primes:
        ans +=1
    t//=10
print(ans)
