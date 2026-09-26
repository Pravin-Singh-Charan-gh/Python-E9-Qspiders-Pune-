##Exercise 8: List Comprehension Filtering (Advanced)
##Practice Problem: Given a list of strings, use a single list comprehension to extract strings that meet two criteria: they must be longer than 5 characters AND they must start with a vowel (a, e, i, o, u).

words = eval(input('Enter the list of strings : '))
print([word for word in words if len(word)>5 and word[0] in 'AEIOUaeiou'])
        
