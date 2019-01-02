# In this we will be seeing how instance Attributes are used
# Instance attributes are accessed by: object.attribute
# Attributes are looked First in the instance and THEN in the class

import random


class Vehicle():
    # Class Methods/ Attributes
    def type_of_vehicle(self):
        # NOTE: This is not a class attribute as the variable is bound to self.
        # Hence it becomes instance attribute
        # randomValue is a variable
        self.randomValue = random.randint(1, 10)  # Setting the instance attribute


motor = Vehicle()
motor.type_of_vehicle()  # Calling the class Method
# print(motor.randomValue)  # Calling the instance attribute
