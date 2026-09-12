#WAP to reverse the original list

my_list = eval(input('Enter the list : '))



#For loop
i = len(my_list)-1
for i in range(len(my_list)//2):
    j = -(i+1)
    my_list[i],my_list[j]=my_list[j],my_list[i]
print(my_list)

#While loop
i = 0
j = len(my_list)-1

while i<j:
    my_list[i],my_list[j]=my_list[j],my_list[i]
    i+=1
    j-=1

print(my_list)
