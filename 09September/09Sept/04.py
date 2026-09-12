#WAP to convert integer to binary using while loop

n = int(input('Enter a number : '))

temp = n
binary = ''

while temp:
    rem = temp%2
    binary = str(rem)+binary
    temp//=2
print(binary)