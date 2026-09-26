# Exercise 19. Armstrong Number Check
# Practice Problem: Write a program to check if a number is an Armstrong number. An Armstrong number (for a 3-digit number) is an integer such that the sum of the cubes of its digits is equal to the number itself (e.g., 153 = 1^3 + 5^3 + 3^3).

n = int(input('Enter the number : '))

t = n
power = 0
while t:
    power+=1
    t//=10 

t = n
s = 0

while t:
    dig = t%10
    s+=dig**power
    t//=10
if n==s:
    print('Armstrong')
else:
    print('Not Armstrong')