##16.	Given a number, print “Weird” if it’s odd or in range 6–20 even. Otherwise print “Not Weird”. (Classic hackerrank logic twist)

n = int(input('Enter the number : '))

if n%2 or 6<=n<=20:
    print('Weird')
else:
    print('Not Weird')