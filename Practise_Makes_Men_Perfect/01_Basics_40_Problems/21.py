#Print a downward half-pyramid pattern using stars (*).

def rev_half_pyramid(n):
    for i in range(n,0,-1):
        print('* '*i)

n = int(input('Enter the number to print reverse pyramid pattern : '))

rev_half_pyramid(n)