# Exercise 15. String Partitioning
# Practice Problem: Use the .partition() method to split a string into three parts: the part before a separator, the separator itself, and the part after it.

txt = input('Enter the string : ')
sep = input('Enter the partition : ')

ans = txt.partition(sep)

print(ans)