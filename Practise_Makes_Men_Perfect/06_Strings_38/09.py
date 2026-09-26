##Exercise 9. String characters balance test
##Practice Problem: Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in s1 are present in s2. The character’s position doesn’t matter.
##

def is_balanced(s1,s2):
    
    for ch in s1:
        if ch not in s2:
            return False
    return True
            

s1 = input('Enter first string : ')
s2 = input('Enter second string : ')

print("Is s1 and s2 balanced:", is_balanced(s1, s2))