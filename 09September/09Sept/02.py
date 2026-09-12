#WAP to create a list of odd numbers, even numbers using while loop

start = int(input('Enter the start number : '))
end = int(input('Enter the end number : '))

odds = []
evens = []

while start<=end:
    if start%2:
        odds.append(start)
    else:
        evens.append(start)
    start+=1
print('Odd Numbers : ',odds)
print('Even Numbers : ',evens)
