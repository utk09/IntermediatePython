class a_simple_class():
    pass


class MyFirstClass():
    # Class Attributes
    var = 10
    var2 = 20
    name = str("Ryuk")


firstObject = MyFirstClass()
print(firstObject.var)  # Accessing Class Attributes

secondObject = MyFirstClass()
print(secondObject.var2)

thirdObject = MyFirstClass()
print(thirdObject.name)

