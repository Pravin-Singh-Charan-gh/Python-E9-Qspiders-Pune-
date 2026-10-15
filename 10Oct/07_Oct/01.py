#SUm of n natural numbers

def n_sum(n):
    if n<=0:
        return 0
    return n+n_sum(n-1)

print(n_sum(10))