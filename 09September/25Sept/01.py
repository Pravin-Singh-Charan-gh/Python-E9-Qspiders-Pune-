#WAP to validate 2 matrix are valid and similar or not

m1 = eval(input('Enter the first matrix : '))
m2 = eval(input('Enter the second matrix : '))

if len(m1)== len(m2):
    for (i,j) in zip(m1,m2):
        if len(i)!=len(m1[0]) or len(i) != len(j):
            print('Not Valid')
            break
    else:
        print('Valid')
else:
    print('Not Valid')
