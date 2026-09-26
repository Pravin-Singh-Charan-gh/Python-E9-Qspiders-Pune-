##Exercise 35. Digit Detection in Strings
##Practice Problem: Write a program to check if a user-entered string contains any numeric digits. Use a for loop to examine each character.

def has_digit(txt):
    for ch in txt:
        if '0'<=ch<='9':
            return True
    return False
txt = input('Enter the String : ')
if has_digit(txt):
    print('Yes')
else:
    print('No')
            
