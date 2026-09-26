##18.	Convert decimal to binary manually.

n = int(input('Enter the number : '))

binary = ''

t = n

while t:
    rem = t%2
    binary = str(rem)+binary
    t//=2
print(binary)
