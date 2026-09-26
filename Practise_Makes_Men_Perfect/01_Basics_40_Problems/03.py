#Display only those characters which are present at an even index number in given string.

txt = input('Enter the string : ')

for i in txt[::2]:
    print(i)
