# class method``
class Demo:
    a = 10
    b = 20

    @classmethod 
    def change_a(cls,value):   #class will be passed as a argument
        print(cls)
        cls.a = value 

    def fun(self):
        pass

obj = Demo()
print('Before Modifying')
print('obj :',obj.a)
print('class :',Demo.a)

Demo.change_a(100)

print('After Modifying through class')
print('obj :',obj.a)  #100
print('class :',Demo.a) #100
obj.change_a(200)

print('After Modifying through object')    #classmethod will try to find reference class of that object
print('obj :',obj.a)  #200
print('class :',Demo.a) #200