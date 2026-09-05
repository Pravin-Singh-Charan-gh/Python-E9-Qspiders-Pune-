# WAP to print the sum of first n numbers if the number is even else print odd

n = int(input("Enter a number : "))

if n%2==0:
    ans = n*(n+1)//2
    print(ans)

else:
    print("odd")
