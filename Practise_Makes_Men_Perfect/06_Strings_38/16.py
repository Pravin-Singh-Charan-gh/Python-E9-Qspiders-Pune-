# Exercise 16. Extract File Extension
# Practice Problem: Given a filename as a string, extract only the file extension (e.g., .png or .pdf).

file_name = input('Enter the file name : ')

last_dot = file_name.rfind('.')
print(file_name[last_dot+1:])
# OR
print(file_name.split('.')[-1])