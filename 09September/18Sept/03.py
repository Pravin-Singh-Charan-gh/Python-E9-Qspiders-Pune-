## LCM

n1 = int(input('Enter the first number : '))
n2 = int(input('Enter the second number : '))

r = abs(n1-n2)
for i in range(1,r+1):
    if n1%i==0 and n2%i==0:
        gcd = i
## no need to declare gcd
print('LCM :',(n1*n2)//gcd)


## My method
t1,t2=n1,n2
curr = 2
lcm = 1
while t1!=1 or t2!=1:
    if 
    
