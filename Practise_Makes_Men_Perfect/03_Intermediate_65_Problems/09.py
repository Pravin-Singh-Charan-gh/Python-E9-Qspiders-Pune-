##Exercise 9: Remove Duplicates (Preserving Order)
##Practice Problem: Write a function that removes duplicate elements from a list. You cannot use set() because sets do not maintain the original order of elements.

def remove_duplicates(l):
    seen= set()
    ans = []
    for i in l:
        if i not in seen:
            ans.append(i)
            seen.add(i)
    return ans
l = eval(input('Enter the list : '))
print(remove_duplicates(l))
