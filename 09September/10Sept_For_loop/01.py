words = input('Enter the string : ')
words = words.split()

words = words[::-1]
for i in words:
    print(i,end=' ')
