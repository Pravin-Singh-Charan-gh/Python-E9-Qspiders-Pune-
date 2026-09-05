marks = int(input('Enter the marks : '))

if 0<=marks<=100:
    if marks >=90:
        print('A')
    elif marks>=80:
        print('B')
    elif marks>=65:
        print('C')
    elif marks>=40:
        print('D')
    else:
        print('FAIL')
else:
    print('Your examiner is bojh on dharti')
