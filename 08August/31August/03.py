# WAP to check whether the number is power of 2 or not

# print(2**7888)

n = int(input("Enter a number : "))

if n & n-1==0:
    print("YES")

else:
    print("NO")