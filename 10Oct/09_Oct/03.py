#WAP to check wheter the  no. is armstrong no. or not using recursion

def isArmstrong(n):
    power = len(str(n))
    return n==sum_of_powers(n,power)

def sum_of_powers(n,power):
    if not n:
        return 0
    last = n%10
    return last**power + sum_of_powers(n//10,power)

print(isArmstrong(150))
print(isArmstrong(153))
