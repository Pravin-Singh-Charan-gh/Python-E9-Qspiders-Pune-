# Exercise 16. Transform a List Using Lambda and map()
# Practice Problem: Use the map() function and a lambda to double every element in the list [1, 2, 3, 4, 5].

nums = [1, 2, 3, 4, 5,111]

ans = list(map(lambda x:x*2,nums))

print(ans)