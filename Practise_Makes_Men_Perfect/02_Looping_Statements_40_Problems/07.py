## Exercise 7. Display numbers from a list using a loop
## Practice Problem: Given a list of numbers, iterate through it and print numbers that satisfy these conditions:
## The number must be divisible by five.
## If the number is greater than 150, skip it and move to the next.
## If the number is greater than 500, stop the loop entirely.

l = eval(input('Enter the list : '))

for i in l:
    if i>500:
        break
    elif i>150:
        continue
    elif not i%5:
        print(i)
    
