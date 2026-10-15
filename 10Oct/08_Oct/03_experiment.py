def n_num(n,i=1):
    if i>=n:
        return
    print(i,end =' ',flush=True)
    n_num(n,i+1)

n_num(10000)
