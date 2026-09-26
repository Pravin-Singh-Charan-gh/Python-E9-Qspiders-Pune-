##Exercise 8. Count occurrences of a specific element in a list
##Practice Problem: Given a list of numbers, use a loop to count how many times a specific number (e.g., 10) appears.

def count_occ(l,k):
    ans=0
    for i in l:
        if i==k:
            ans+=1
    return ans

l = [10, 20, 10, 30, 10, 40, 50]
target = 10

print(f"{target} appears {count_occ(l,target)} times")