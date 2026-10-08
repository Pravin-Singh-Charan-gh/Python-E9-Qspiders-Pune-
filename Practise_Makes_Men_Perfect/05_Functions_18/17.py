# Exercise 17. Sort Complex Data with sorted() and Lambda
# Practice Problem: You have a list of tuples representing students and their grades: [("Alice", 88), ("Bob", 75), ("Charlie", 92)]. Use the sorted() function and a lambda to sort this list based on the grades (the second element) in ascending order.

t = [("Alice", 88), ("Bob", 75), ("Charlie", 92)]
ans = sorted(t,key=lambda student:student[1])

print(ans)