# Classes and Variables

class Dog:
    # class variables are like static variables
    doginfo = "Dogs are animals with 4 legs and a tail"

    # init method will be called every time you create an instance of this class
    # similar to constructor
    def __init__(self, name, age, color):
        print("instance created")
        # create instance variables from input parameters
        self.name = name
        self.age = age
        self.color = color

    @staticmethod
    def staticMethod():
        print("this is a static method")

    # class method can only be called using Dog class
    @classmethod
    def classMethod(cls):
        print("this is a class method, {}".format(cls))

    # instance method can only be called using instance of the class
    # instance method has input parameter self
    def instanceMethod(self):
        print("this is an instance method, {}".format(self))


class Bulldog(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)

    def growl(self):
        print("GRRRRRR")


dog2 = Bulldog("yuan", 16, "red")
dog2.growl()


# you can access to class variables without having to create an instance
print(Dog.doginfo)

dog1 = Dog("nancy", 15, "blue")

print(dog1.name)

# instance variables can be created on the fly
dog1.random = "random"


# https://realpython.com/instance-class-and-static-methods-demystified/#instance-methods
# Instance methods need a class instance and can access the instance through self.
# Class methods don't need a class instance. They can't access the instance (self) but they have access to the class itself via cls.
# Static methods don't have access to cls or self. They work like regular functions but belong to the class's namespace.
# Static and class methods communicate and (to a certain degree) enforce developer intent about class design. This can have maintenance benefits.


dog1.instanceMethod()
dog1.classMethod()
dog1.staticMethod()

# Dog.instanceMethod()
Dog.classMethod()
Dog.staticMethod()
