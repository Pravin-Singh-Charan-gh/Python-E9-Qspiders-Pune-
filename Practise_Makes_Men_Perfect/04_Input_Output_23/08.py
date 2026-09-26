##Exercise 8. Percentage display
##Practice Problem: Ask the user for a numerator and a denominator. Calculate the percentage (numerator/denominator * 100) and display it with exactly two decimal places followed by a percent sign.

num = int(input('Enter the numerator : '))
deno = int(input('Enter the denominator : '))

perc = (num/deno)*100
print(f"The result is : {perc:.2f}%")
