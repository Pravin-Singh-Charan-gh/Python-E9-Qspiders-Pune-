# Exercise 20. Remove Duplicates from List
# Practice Problem: Remove all duplicate values from a list while keeping only one instance of each element.

duplicates = [10, 20, 10, 30, 40, 40, 20, 50]

# Method to remove duplicates while preserving order
unique_list = list(dict.fromkeys(duplicates))

print(f"Unique List: {unique_list}")