##17.	University admission logic (cutoff + entrance test + reserved category).

reserved_cutoff= 45
no_reverved_cutoff = 50

marks = int(input('Enter marks : '))
entrance_score = int(input('Enter Entrance Score : '))
is_reserved = input('Is category reserved : ').lower()

if is_reserved=='yes':
    if entrance_score>=45:
        if marks>=50:
            print('Admission Granted')
        else:
            print('Admission Rejected')
    else:
            print('Admission Rejected')
else:
    if entrance_score>=50:
        if marks>=55:
            print('Admission Granted')
        else:
            print('Admission Rejected')
    else:
            print('Admission Rejected')