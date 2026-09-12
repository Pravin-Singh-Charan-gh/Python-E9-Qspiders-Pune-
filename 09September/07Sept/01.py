#reverse a string

s = input('Enter the string : ')


ans = ''
i=0
while i<len(s):
    ans=s[i]+ans
    i+=1
print(ans)
