#In a given list of strings,skip all the palindromic strings and print other strings

strs = eval(input('Enter the list of strings : '))

for txt in strs:
    if txt==txt[::-1]:
        continue
    print(txt)
