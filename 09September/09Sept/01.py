#Range#



#WAP to generate list of natural numbers from 1 to n using while loop

n = int(input('Enter the number : '))

ans = []
i = 1 
while i<=n:
    ans.append(i)
    i+=1
print(ans)