#Calculate income tax for a given income based on these rules:
##First $10,000: 0% tax
##Next $10,000: 10% tax
##Remaining income: 20% tax

def income_tax(income):
    if income<=10000:
        return 0

    elif 10000<income<=20000:
        return (income-10000)*0.1

    else:
        return 10000*0.1 + (income-20000)*0.2

income = int(input('Enter the income : '))
print(income_tax(income))
