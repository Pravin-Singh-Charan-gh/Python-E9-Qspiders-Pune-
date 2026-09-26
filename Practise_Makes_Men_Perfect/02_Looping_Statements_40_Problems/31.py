# Exercise 31. Even/Odd Segregation: Move evens to front, odds to back
# Practice Problem: Given a list of integers, move all even numbers to the beginning of the list and all odd numbers to the end.

l = [1, 2, 3, 4, 5, 6]
evens=0

for i in l:
    if i%2==0:evens+=1

ans = [0]*len(l)
even_index = 0
odd_index = evens

for i in l:
    if i%2:
        ans[odd_index]=i 
        odd_index+=1
    else:
        ans[even_index]=i
        even_index+=1
print(ans)

# 5