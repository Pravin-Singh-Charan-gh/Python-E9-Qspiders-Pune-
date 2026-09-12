#find the second largest number in a tuple

t = (1,20,21,30,6,45,9,12)
largest = t[0]
second_largest = t[0]

i = 0
while i < len(t):
    if t[i] > largest:
        largest,second_largest=t[i],largest
    elif t[i]>second_largest:
        second_largest=t[i]
    i+=1
print(second_largest)