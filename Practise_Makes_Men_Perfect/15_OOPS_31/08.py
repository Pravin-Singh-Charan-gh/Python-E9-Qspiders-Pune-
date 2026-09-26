##Exercise 8: User Class with Password Validation
##Problem Statement: Write a Python program to create a User class that stores a username and a password. Add a check_password(input_password) method that returns True if the input matches the stored password, and False otherwise.

class User:
    def __init__(self,username,password):
        self.username= username
        self.password = password

    def check_password(self,input_password):
        return self.password == input_password

u1 = User('Pravin',1233)
print(u1.check_password('7623'))
