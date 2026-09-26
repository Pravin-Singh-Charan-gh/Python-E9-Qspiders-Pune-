# Exercise 16. Turn Every Item of a List into its Square (List Comprehension)
# Practice Problem: Given a list of numbers, create a new list where each number is replaced by its square (n2) using a single line of code.

l = eval(input('Enter the list : '))

ans = [i**2 for i in l]
print(ans)