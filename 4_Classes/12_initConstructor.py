# Use of __init__ constructor

class Vehicle():
    # __init__ is used to set values as soon as new object are created
    # __init__ is a keyword hence it has to be named like it is
    def __init__(self):  # called automatically hence known as magic method
        print('Calling init')
        self.val = 0
        self.cost = 10000  # Setting the default value when the object is created

    def incrementVehicle(self):
        self.val += 10


car = Vehicle()  # __init__ is called
print('First object(car) value:', car.val)
car.incrementVehicle()  # 1
car.incrementVehicle()  # 2
print('First object value after incrementing twice:', car.val)
car.incrementVehicle()  # 3
print('First object value after incrementing one more time:', car.val)
car.incrementVehicle()  # incremented once more # 4
print("------------------------------------------")

scooty = Vehicle()  # __init__ is called, makes 'val' 0 for this ANOTHER instance
print('Second object(scooty) value:', scooty.val)
print('Second object cost:', scooty.cost)
print("------------------------------------------")

print('First object(car) value after calling "scooty" instance:', car.val)
