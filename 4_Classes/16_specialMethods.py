'''
In Python you can define a method in such a way that there are multiple ways to call it.
Given a single method or function, we can specify the number of parameters ourself.
Depending on the function definition, it can be called with zero, one, two or more parameters.
This is known as method overloading. Not all programming languages support method overloading, but Python does.
'''


# In this example we will see what are Python Magic Methods (or Special Methods) and how to overload them
# The reason is these are called Magic Methods or Special Methods is because these
# methods are invoked directly after creation of a class instance.
# For example: __init__ is a Magic method. Also __str__, __repr__, __add__ are all magic methods.

class Employee(object):
    def __init__(self, firstname, lastname, salary=0):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    def __str__(self):
        return 'Full Name: ' + self.firstname + ' ' + self.lastname

    # For overloading the (+)
    def __add__(self, other):
        return self.salary + other.salary

    # For overloading the (*)
    def __mul__(self, other):
        return self.salary * other.salary


if __name__ == '__main__':
    Conan = Employee('Shinichi', 'Kudo', 1000)
    Kaleen = Employee('Akhandanand ', 'Tripathi', 2000)
    print(Conan)  # Full Name: Shinichi Kudo (This output because of __str__ method overloading)
    print(Kaleen)  # Full Name: Akhandanand  Tripathi
    print("Conan + Kaleen: ", Conan + Kaleen)  # 3000 (This output because of __add__ method overloading)
    print("Conan * Kaleen: ", Conan * Kaleen)  # 2000000 (__mul__ method overloading)
