#Exercise 31. Print Alternate Prime Numbers
#Practice Problem: Write a program to find all prime numbers up to 20, but only print every second (alternate) prime number found.

def alt_prime(n):
    do_print = True
    for i in range(1,21):
        if is_prime(i):
            if do_print:
                print(i)
                do_print = False
            else:
                do_print = True
def is_prime(n):
    if n==1:return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

alt_prime(20)
