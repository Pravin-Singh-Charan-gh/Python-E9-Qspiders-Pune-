# Grade system based on marks (90+, 75+, 50+, else fail).

marks = int(input('Enter the marks : '))

if marks<0 or marks >100:
    print('Inalid Marks')
elif marks>90:
    print('A Grade')
elif marks>75:
    print('B Grade')
elif marks>50:
    print('C Grade')
else:
    print('Fail')