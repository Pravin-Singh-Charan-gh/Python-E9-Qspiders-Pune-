# Exercise 9. Find the Largest Item in a List
# Practice Problem: Create a function that takes a list of numbers as input and returns the largest item from that list without using the built-in max() function (to practice manual logic).

def max_int(l):
    if not l:
        return None

    maxi = -float('inf')
    for i in l:
        if i>maxi:
            maxi =i
    return maxi

print(max_int([4, 6, 8, 24, 12, 2]))