#Abstraction
#Encasulation
#Polymorphism
#Inheritance

#Encasulation
student1={
    "name":"Jatin Katyal",
    "Marks":50
}
student2={
    "name":"samarth",
    "Marks":100
}

class Person:
    pass
p=Person() #If we call a class it will create new object of the class
print(p)
print(hex(id(p)))


class Person:
    name="Jatin"
    def say_hi(self):
        print(f"Hello Everyone! I am {self.name}")
p=Person()
p.say_hi() #Python automatically places this p as the 1st argument, this means that this function is being treated as a method
Person.say_hi(p)

class Person:
    name="Jatin"
    def say_hi(thisS):
        print(f"Hello Everyone! I am {self.name}")
p=Person()
p.say_hi() #Method Call
Person.say_hi(p) #Function Call
