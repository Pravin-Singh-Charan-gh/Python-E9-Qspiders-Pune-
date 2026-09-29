#WAP to check if the number is strong number or not

def fact(n):
    ans = 1
    while n:
        ans*=n
        n-=1
    return ans

def is_strong(n):
    """It checks whether the number is strong or not"""

    res = 0
    t = n
    while t:
        last = t%10
        res += fact(last)
        t//=10
    return res==n 


# n = int(input('Enter the number : '))

# if is_strong(n):
#     print(f'{n} is a strong number')
# else:
#     print(f'{n} is not a strong number')
i=1
curr = 1
while i<=10:
    if is_strong(curr):
        print(curr)
        i+=1
    curr+=1