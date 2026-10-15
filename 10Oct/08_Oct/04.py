def fun():
    global x
    x+=1
    fun()
x=1
fun()
