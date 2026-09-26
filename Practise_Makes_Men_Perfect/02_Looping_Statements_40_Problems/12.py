# Exercise 12. Count vowels and consonants in a sentence
# Practice Problem: Write a program that counts the total number of vowels and consonants in a given sentence, ignoring spaces and special characters.

sent = "Loops are Fun!"
vow = 0
cons = 0

for ch in sent:
    if ch in 'AEIOUaeiou':
        vow+=1
    elif 'A'<=ch<='Z' or 'a'<=ch<='z':
        cons+=1
print('Vowerl :',vow)
print('Consonents :',cons)