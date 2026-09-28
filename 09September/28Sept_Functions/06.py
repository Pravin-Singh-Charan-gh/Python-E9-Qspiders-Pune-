#WAP to reverse a string without slicing

def rev_str(s):
    ans=''
    for ch in s:
        ans = ch+ans
    return ans

s = input('Enter the string : ')
rev = rev_str(s)
print(rev)