#class
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def me(self):
        print("My name is ",self.name)
#object
p1=Person("adi","20")
print(p1.age)
p1.me()

# It does not have to be named self , you can call it whatever you like,
# but it has to be the first parameter of any function in the class:

class Person:
    def __init__(sugu,name,age):
        sugu.name=name
        sugu.age=age
    def me(sugu):
        print("My name is ",sugu.name)
        
p1=Person("adi","20")
print(p1.age)
p1.me()
