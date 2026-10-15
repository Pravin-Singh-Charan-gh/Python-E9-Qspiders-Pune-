def fun(n,i=1):
    if i==n:
        print(i,end=' ')
        return
    print(i,end=' ')
    fun(n,i+1)
    print(i,end=' ')
    
fun(3)
