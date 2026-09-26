#Write a function to remove characters from a string starting from index 0 up to n and return a new string.

def remove_chars(txt,n):
    return txt[n+1::]

txt = input('Enter the string : ')
n = int(input('Enter the index to remove characters till : '))

ans = remove_chars(txt,n)

print(ans)
