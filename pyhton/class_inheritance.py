class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def me(self):
        print("My name is ",self.name)

class Student(Person):
    pass
Student("adi","20").me()
