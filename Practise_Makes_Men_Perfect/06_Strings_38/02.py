##Exercise 2. Create a string made of the middle three characters
##Practice Problem: Write a program to create a new string made of the middle three characters of an input string of odd length.

txt = input('Enter the string : ')
l = len(txt)
ans = txt[l//2-1:l//2+2]  #las is excluded
print(ans)
