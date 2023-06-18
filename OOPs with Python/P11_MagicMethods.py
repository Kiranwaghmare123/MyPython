
# In this example we will see what are Python Magic Methods (or Special Methods) and how to overload them
# Now why these methods are called Magic or Special methods anyway? The reason is that these
# methods are invoked directly after creation of a class instance. For example:
# __init__ is a Magic method. Also __str__, __repr__, __add__ are all magic methods.

class Employee(object):
    def __init__(self, firstname, lastname, salary = 0):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    def __str__(self):
        return 'Full Name: ' + self.firstname + ' ' + self.lastname

    # Implements behaviour for built in type comparison to int
    def __int__(self):
        return self.salary

    # For overloading the (==)
    def __eq__(self,other):
       return self.salary==other.salary   

    # For overloading the (+)
    def __add__(self, other):
        return self.salary + other.salary

    # For overloading the (*)
    def __mul__(self, other):
        return self.salary * other.salary

if __name__ == '__main__':
    Kiran = Employee('Kiran', 'Waghmare', 1000)
    Ram = Employee('Ram ','Verma', 2000)
    print(Kiran)                # Full Name: Kiran Waghmare (This output because of __str__ method overloading)
    print(Ram)              # Full Name: Ram Verma
    print(Kiran + Ram)      # 3000 (This output because of __add__ method overloading)
    print(Kiran * Ram)      # 2000000 (__mul__)
    print(int(Kiran))           # 1000 (__int__)
    print(int(Ram))         # 2000 (__int__)
    print(Kiran==Ram)
