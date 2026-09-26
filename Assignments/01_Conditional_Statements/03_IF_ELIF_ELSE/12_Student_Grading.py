#12.	Student grading with distinction logic (90+, 75+, 50+, borderline 48–49 → re-evaluation).

marks = int(input('Enter marks : '))

if marks<0 or marks>100:
    print('Invalid Marks')
elif marks>90:
    print('A Grade')
elif marks>75:
    print('B Grade')
elif marks>50:
    print('C Grade')
elif marks in (48,49):
    print('Re-evaluation')
else:
    print('Fail')