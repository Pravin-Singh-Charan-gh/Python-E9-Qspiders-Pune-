# WAP to print the sum of digits

def sum_of_digits(n):
    if not n:
        return 0
    return n%10 + sum_of_digits(n//10)

n = int(input('Enter the number : '))

print(sum_of_digits(n))