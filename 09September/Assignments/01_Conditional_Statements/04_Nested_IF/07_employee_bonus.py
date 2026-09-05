##7.	Employee bonus eligibility (experience → performance rating).

exp = int(input('Enter experience : '))
performance_rating = int(input('Enter rating out of 5 : '))

if exp >=2 and performance_rating>=4:
    print('Eligible for Bonus')
else:
    print('Not eligible for Bonus')
    