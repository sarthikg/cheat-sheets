# Defining a Class
class Employee:
    # Init Function will run for every object created with this Class by default
    def __init__(self, firstName, lastName, age):
        
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

