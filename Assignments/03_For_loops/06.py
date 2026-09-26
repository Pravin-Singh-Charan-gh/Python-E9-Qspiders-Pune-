# 6. Reverse a string using loop.

txt = input('Enter the string : ')
rev = ""

for i in range(len(txt)):
    rev = txt[i]+rev

print(rev)