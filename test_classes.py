import math

from arthmetic import *;
'''
Classes can represent real-world objects or abstract ideas. After defining a class, you use it by making an instance, or object,of the class. You can make as many instances as you want from one class.
As an example, you might use a class to represent a website user. The class would have attributes associated with the user’s username, password, registration date, and more. Methods would define the actions the user could take, such as registering, authenticating, logging in, and logging out. You could then make one instance for each user who registers on the site.
Many external libraries are written as classes, so learn-ing to work with classes makes it easier to work with many existing projects.
'''

ar = Arithmetic()
print(ar.add())
print(ar.divide())
print(ar.remainder())
ar.print_self()

#TODO: create several more instance of the Arithmetic class and add different values

class Arithmetic:

    def __init__(self, number1 = 3, number2 = 6):
        if(number1 > number2):
            self.number2 = number1
            self.number1 = number2
        else:
            self.number1 = number1
            self.number2 = number2

    def add_then_double(self):
        return (self.number1 + self.number2)*2

    def add_then_square(self):
        return (self.number1 + self.number2)**2

    def add_then_square_root(self):
        return math.sqrt(self.number1 + self.number2)

