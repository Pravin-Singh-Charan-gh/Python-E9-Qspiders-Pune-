#WAP to convert integer into binary

n = int(input('Enter the number : '))

temp = n

ans = ''
while temp:
    r = temp%2
    ans = str(r)+ans
    temp//=2
print(ans)
