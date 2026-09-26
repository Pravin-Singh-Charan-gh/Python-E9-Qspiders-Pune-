# Exercise 6. Count Even and Odd Numbers
# Practice Problem: Given a list of integers, iterate through the items and count how many are even and how many are odd.

l = eval(input('Enter the list : '))
evens = 0
odds = 0

for i in l:
    if i%2:
        odds+=1
    else:
        evens+=1

print('Number of Evens :',evens)
print('Number of Evenes Odds :',odds)