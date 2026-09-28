#WAP to check whether the number is odd or even

def odd_even(n):
    """ it check whether the number is odd or even"""
    if n%2:
        return "odd"
    return 'even'

n = int(input('Enter the number : '))
print(f'{n} is a {odd_even(n)} number ')
