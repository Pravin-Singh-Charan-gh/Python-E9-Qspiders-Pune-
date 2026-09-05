#WAP TO CHECK WHETHER THE 2 DIGIT NUMBER IS PALINDROME OR NOT

n = int(input("Enter a number : "))

##if n[0]==n[1]:
#   print("YES")
#else :
#    print("NO")

if 9<n<100 and n%11==0:
    print("YES")
else:
    print("NO")
