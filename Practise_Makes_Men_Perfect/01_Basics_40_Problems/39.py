##Exercise 39. External File Word Counter
##Practice Problem: Write a script that opens an existing .txt file and counts the total number of words it contains.

file = open('notes.txt','r')

content = file.read()

print(len(content.split()))
