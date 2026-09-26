# 15.	BMI calculator with underweight / normal / overweight / obese.

height = float(input('Enter the height in meters: '))
weight = float(input('Enter the weight in kg: '))

bmi = weight/(height**2)

print('BMI : ',bmi)

if bmi<18.5:
    print('Underweight')
elif bmi<25:
    print('Normal')
elif bmi<30:
    print('Overwight')
else:
    print('Obese')