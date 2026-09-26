##Exercise 8. Find all occurrences of a substring in a given string by ignoring the case
##Practice Problem: Write a program to find the total count of the substring “USA” in a given string, ignoring the case (i.e., both “usa” and “USA” should be counted).
##

str1 = "Welcome to USA. usa awesome, isn't it?"
substring = 'USA'
ans = str1.lower().count(substring.lower())

print('Count', ans)
