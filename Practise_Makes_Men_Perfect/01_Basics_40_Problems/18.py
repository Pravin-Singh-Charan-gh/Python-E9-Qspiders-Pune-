# Write a program to extract each digit from an integer in the reverse order.

def digit_extraction(n):
    t = n
    while t:
        print(t%10)
        t//=10
n = int(input('Enter the number : '))

print(digit_extraction(n))
