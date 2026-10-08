#WAP to check if the given all the numbers are palindrome or not

def isPalindrome(*args):
    for i in args:
        if str(i)!=str(i)[::-1]:
            return False
    return True

l1 = [1,2,3,4,5,11,22]
l2 = [11,12,13]

print(isPalindrome(*l1))
print(isPalindrome(*l2))
