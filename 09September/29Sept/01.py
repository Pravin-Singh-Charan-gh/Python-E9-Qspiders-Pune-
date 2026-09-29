#second largest in a list

a = [10,20,40,40]

if len(a)>0:
    l = a[0]
    s = None

    for i in a:
        if i>=l:
            s = l
            l = i
        elif s!=None and i>s and i!=l:
            s = i
        elif s==None and i<l:
            s = i
    print(s)

def sec_max(a):
    if len(a)>0:
        l = a[0]
    s = None

    for i in a:
        if i>=l:
            s = l
            l = i
        elif s!=None and i>s and i!=l:
            s = i
        elif s==None and i<l:
            s = i
    print(s)