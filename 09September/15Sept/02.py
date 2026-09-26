cars  = {
    'Fortuner' : ['Speed','Power','Safety'],
    'Scorpio N' : ['Power', 'Boot space', 'Design']
    }

for car in cars:
    print(car)
    for prop in cars[car]:
        print('\t'+'*'+prop)
