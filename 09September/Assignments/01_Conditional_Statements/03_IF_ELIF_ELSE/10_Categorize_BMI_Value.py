##10.	Categorize BMI value.

bmi = int(input('Enter the BMI Value : '))

if bmi<0:
    print('Invalid BMI Value')
elif bmi<18:
    print('Underweight')
elif bmi<25:
    print('Normal')
elif bmi<30:
    print('Overweight')
else:
    print('Obese')