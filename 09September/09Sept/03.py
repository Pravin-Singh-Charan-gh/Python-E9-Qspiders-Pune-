# I am Yash
# Yash am I

s = input('Enter the string : ')

strings = ['']
i = len(s)-1
while i>=0: 
    if s[i]==' ':
        strings.append('')
    else:
        strings[-1]= s[i]+strings[-1]
    i-=1

i = 0
while i<len(strings):
    print(strings[i],end=' ')
    i+=1

print()

# Single line code
ans = ' '.join(s.split(' ')[::-1])
print(ans)