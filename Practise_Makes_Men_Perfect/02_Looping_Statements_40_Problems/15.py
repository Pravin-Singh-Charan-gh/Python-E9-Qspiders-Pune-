# Exercise 15. Find largest and smallest digit in a number
# Practice Problem: Write a program to find the largest and smallest digit within a given integer (e.g., in 75869, the largest is 9 and the smallest is 5).

n = int(input('Enter the number : '))
small,lar = 9,0

t = n
while t:
    digit = t%10
    small = min(small,digit)
    lar = max(lar,digit)
    t//=10
print('Small :',small)
print('Largest :',lar)