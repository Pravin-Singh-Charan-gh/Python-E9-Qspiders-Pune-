class StateBoard:
    def rules(self):
        return 'Cheating is not allowed'

class School(StateBoard):
    school_name = 'Qspiders'
    loc = 'Wakad'
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Teacher(School):
    def __init__(self,name,age,sub):
        super().__init__(name,age)
        self.sub = sub

obj = Teacher('Vijay',28,'SQL')
