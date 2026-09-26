# Exercise 21. List Comprehension for Filtering Numbers
# Practice Problem: Given a list of integers, use list comprehension to create a new list that contains only the even numbers from the original list.

nums = eval(input('Enter the list : '))

evens = [x for x in nums if x%2==0]
print(evens)