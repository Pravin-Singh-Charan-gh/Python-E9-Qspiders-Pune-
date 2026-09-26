#Create a list of 5 fruits. Add a new fruit to the end of the list, then remove the second fruit (at index 1).

fruits = ['mango','orange','coconut','guava','watermelon']
print(fruits)
fruits.append('date')
print(fruits)

fruits.pop(1)
##or
del fruits[1]

print(fruits)

