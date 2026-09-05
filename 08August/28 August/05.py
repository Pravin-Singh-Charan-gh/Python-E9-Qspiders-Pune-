#WAP to check whether the data is mutable data type or not

# str = input("Enter data : ")

# if str[0] in "[{":
#     print("Yes")
# else:
#     print("No")
    # [iuaushduasd8   and ' [1,2,3]'  space at the beginning will not work

data = eval(input("Enter data : "))

if type(data) in [list,set,dict]:
    print("Yes")
else : 
    print("No")