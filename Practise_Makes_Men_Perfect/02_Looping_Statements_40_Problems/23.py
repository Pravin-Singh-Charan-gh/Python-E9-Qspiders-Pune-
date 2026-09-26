# Exercise 23. Print Alphabet pyramid (A, BB, CCC) pattern
# Practice Problem: Write a program to print a triangle pattern where each row consists of the same letter, and the letter changes (increments) with each new row.

# A 
# B B 
# C C C 
# D D D D 
# E E E E E

n = int(input('Enter the number : '))

ch_ascii = 65
for i in range(n):
    ch = chr(ch_ascii+i)
    for j in range(i+1):
        print(ch,end=' ')
    print()

# 6.58