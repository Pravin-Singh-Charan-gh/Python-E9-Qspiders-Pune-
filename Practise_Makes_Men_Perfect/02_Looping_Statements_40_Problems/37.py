# Exercise 37. Display all prime numbers within a range
# Practice Problem: Write a program to display all prime numbers within a range (e.g., 25 to 50). A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.

start = int(input('Enter the start : '))
end = int(input('Enter the end : '))

def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False 
    return True

for i in range(start,end+1):
    if(is_prime(i)):
        print(i)