#WAP to check if the string is palindrome or not without slicing

txt = input('Enter the string  : ')

#USing while loop
i = 0
j = len(txt)-1

is_palindrome = True

while i<j:
    if txt[i]!=txt[j]:
        is_palindrome=False
    i+=1
    j-=1
if is_palindrome:
    print('Palindrome')
else:
    print('Not palindrome')

###########################################
# Using for loop
    
i = len(txt)-1
for j in range(len(txt)//2+1):
    if txt[i]!=txt[j]:
        is_palindrome=False
    i-=1
    
if is_palindrome:
    print('Palindrome')
else:
    print('Not palindrome')
