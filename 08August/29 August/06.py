#WAP to print the FIZZ when the number is divisible by 3 or print the BUZZ is divisible by 5 or print FIZZBUZZ when the numbe is divisble by 3 and 5

n = int(input("Enter a number : "))

if n%3==0 and n%5==0:
    print("FIZZBUZZ")
elif n%3==0:
    print("FIZZ")
elif n%5==0:
    print("BUZZ")