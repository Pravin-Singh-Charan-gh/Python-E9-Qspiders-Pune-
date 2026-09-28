#WAP to print 10 palindrome numbers

def isPalindrome(n):
##    t = n
##    rev = 0
##
##    while t:
##        rem = t%10
##        rev=rev*10+rem
##        t//=10
##    return rev==n

    #2nd approach
    return str(n)==str(n)[::-1]

n = int(input('Enter the number : '))

num = 1
count = 0
while count<n:
    if isPalindrome(num):
        print(num)
        count+=1
    num+=1
