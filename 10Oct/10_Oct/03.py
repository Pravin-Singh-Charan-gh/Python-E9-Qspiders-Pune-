#WAP reverse a number

def rev_num(n,rev=0):
    if n==0:
        return rev
    rem = n%10
    rev = rev*10 + rem
    return rev_num(n//10,rev)

print(rev_num(123))
