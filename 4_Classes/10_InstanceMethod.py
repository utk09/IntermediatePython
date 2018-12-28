class Vehicle():
    # Class Methods/ Attributes

    # Here self is passed as an argument because instance is passed as first argument
    def type_of_vehicle(self):  # Without self it throws an error
        print('I have a scooty')
        print("Vidit has a car")

    # print(2*4) # uncomment, you'll see this runs first


motor = Vehicle()
# print(motor)  # Print Memory location of "motor"
motor.type_of_vehicle()
