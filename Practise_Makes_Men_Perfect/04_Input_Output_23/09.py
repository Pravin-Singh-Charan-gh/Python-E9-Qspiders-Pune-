##Exercise 9: Display right-aligned output
##Practice Problem: Ask the user for a word and a number. Print the word right-aligned in a total field width of 20 characters, followed by the number.

word = input('Enter the word : ')
num = input('Enter the number : ')

print(f"{word:>20} {num}")
