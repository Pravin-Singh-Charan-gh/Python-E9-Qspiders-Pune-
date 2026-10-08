# Exercise 15. Filter a List Using Lambda and filter()
# Practice Problem: Use the filter() function combined with a lambda to extract all even numbers from the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(filter(lambda x:x%2==0,nums))

print(evens)