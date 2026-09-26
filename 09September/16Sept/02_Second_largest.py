# Second largest in the list

l = eval(input('Enter the list : '))

largest = -float('inf')
sec_lar = -float('inf')

for i in l:
    if i > largest:
        sec_lar=largest
        largest=i
    elif i>sec_lar:
        sec_lar=i
print(sec_lar)