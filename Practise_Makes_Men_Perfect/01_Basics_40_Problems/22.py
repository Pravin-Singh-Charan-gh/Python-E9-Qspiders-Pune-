#Write a function called exponent(base, exp) that returns an integer value of the base raised to the power of the exponent.

def exponent(base ,exp):
    ans=1
    for i in range(exp):
        ans*=base
    return ans
base = int(input('Enter the base : '))
exp = int(input('Enter the exponent : '))

print(exponent(base,exp))