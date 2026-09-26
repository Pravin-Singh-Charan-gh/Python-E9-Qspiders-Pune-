##Exercise 36. Capitalize First Letter (Title Case)
##Practice Problem: Write a program to capitalize the first letter of each word in a given string without using the built-in .title() method

def capitalize(txt):
    words = txt.split()
    ans = ''
    for i in range(len(words)):
        ans = ans + ' ' + words[i].capitalize()
##        first_ch = words[i][0]
##        if 'a'<=first_ch<='z':
##            first_ch = first_ch - 32
##            words[i] = first_ch + words[i][1::]
    return ans

txt = input('Enter the text : ')
cap = capitalize(txt)
print(cap)
