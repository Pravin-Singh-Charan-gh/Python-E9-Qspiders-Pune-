#WAP to check if the number is a armstrong number or not

def isArmstrong(n):
    power = len(str(n))
    res = 0
    t = n

    while t:
        last = t%10
        res += last**power
        t//=10

    return res==n

n = int(input('Enter the number : '))
if isArmstrong(n):
    print(f'{n} is a armstrong number.')
else:
    print(f'{n} is not a armstrong number.')
