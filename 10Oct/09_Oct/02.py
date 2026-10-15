#WAP to check whether the number is palindrome or not without loops and typecasting

def reverse_num(n,res=0):
    if n==0:
        return res
    
    rem = n%10
    res = res*10+rem
    return reverse_num(n//10,res)

n = int(input('Enter the number : '))
if n==reverse_num(n):
     print('Palindrome')
else:
     print('Not Palindrome')

##print(reverse_num(n))
