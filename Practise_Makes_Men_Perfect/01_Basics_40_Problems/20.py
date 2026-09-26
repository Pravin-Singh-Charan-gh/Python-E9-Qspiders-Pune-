#Print a multiplication table from 1 to 10 in a formatted grid.

def table_1_10():
    for i in range (1,11):
        for j in range(1,11):
            print(i*j,end='\t')
        print()
table_1_10()
