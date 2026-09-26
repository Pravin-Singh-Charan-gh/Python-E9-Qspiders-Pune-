# Write a program to print the first 15 terms of the Fibonacci series. The sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones.

def feb_n(n):
    a,b=0,1
    print(a)
    print(b)
    for i in range(3,n+1):
        a,b = b,a+b
        print(b)
feb_n(15)
    
    
