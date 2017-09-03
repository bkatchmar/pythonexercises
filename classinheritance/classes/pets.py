class Pet:
    name=""
    age=0
    
    # Base Methods
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return self.firstname + " " + self.lastname
        
    def SaySomething(self):
        return ""

class Dog(Pet):

    def __init__(self, name, age):
        Pet.__init__(self, name, age)
        
    def SaySomething(self):
        return "WOOF WOOF"
    
class Cat(Pet):

    def __init__(self, name, age):
        Pet.__init__(self, name, age)
        
    def SaySomething(self):
        return "meow"