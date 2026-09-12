#WAP to check if the number is armstrong or not

n = int(input('Enter the number : '))

temp = n
digit_count = 0

while temp:
    temp//=10
    digit_count+=1

temp = n
ans=0

while temp:
    rem=temp%10
    ans += rem**digit_count
    temp//=10

if n==ans:
    print('Armstrong')
else:
    print('Not Armstrong')
