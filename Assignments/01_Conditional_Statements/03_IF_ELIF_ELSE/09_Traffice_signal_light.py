##9.	Check traffic signal color (red, yellow, green).

color = input('Enter the color (red,yellow,green): ').lower()

if color=='red':
    print('STOP')
elif color == 'yellow':
    print('Ready to Go!')
elif color=='green':
    print('GO')
else:
    print('Invalid Color')