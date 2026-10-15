# reverse a string using recursion

def rev_str(s,i=0):
    if i==len(s):
        return ''
    return rev_str(s,i+1)+s[i]

s = input('Enter the string : ')
print(rev_str(s))