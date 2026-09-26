# Exercise 9. Print elements from a list present at odd index positions
# Practice Problem: Given a Python list, use a loop to print only the elements that are located at odd index positions (index 1, 3, 5, etc.).

l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(1,len(l),2):
    print(l[i])