# Exercise 11. Prefix/Suffix Check
# Practice Problem: Check if a given URL starts with “https” and ends with “.com”.

url = input('Enter the url : ')

if url.startswith('https') and url.endswith('.com'):
    print('Valid URL')
else:
    print('Not Valid')