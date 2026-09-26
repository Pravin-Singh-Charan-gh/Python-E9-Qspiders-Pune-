##9.	Check if character is alphabet → then check uppercase/lowercase.

ch = input('Enter the character : ')

if len(ch)==1 and ('A'<=ch<='Z' or 'a'<=ch<='z'):
    print('Alphabet Character')
    if ch.islower():
        print('Lowercase')
    else:
        print('Uppercase')
else:
    print('Not Alphabet')