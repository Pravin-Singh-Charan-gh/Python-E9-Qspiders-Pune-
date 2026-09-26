##Exercise 38. File Creation and Basic I/O
##Practice Problem: Write a program that creates a new text file named notes.txt, writes three separate lines of text to it, and then reads that file back to display the contents in the console.

file = open('notes.txt','x')

with open('notes.txt','w') as f:
    f.write("Let's rock!\n")
    f.write("Sun rises in the East\n")
    f.write("Earth Revolves around the Sun")

f = open('notes.txt')
print(f.read())
