# Dunder Methods
    # Example - __init__
        # These methods are used to overwrite the existing default methods in Python
        # Use them with caution only when required

# Private Variables
    # Example - _secret
        # These are a developers way of saying that these should not be accessed and are private
        # Could be accessed though

# Name Mingling
    # Example - __msg
        # These methods are name mingled, or made specific to the class, incase of inheritance
        # Could be accessed by _class__msg


# Defining a Class
class Employee:
    # Init Function will run for every object created with this Class by default
    def __init__(self, firstName, lastName, age):
        # Self Keyword is used to assign class arguments to be used in the class
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
    # 

# Objectifying a Class
employee1 = Employee('Sarthik', 'Gupta', 20)

