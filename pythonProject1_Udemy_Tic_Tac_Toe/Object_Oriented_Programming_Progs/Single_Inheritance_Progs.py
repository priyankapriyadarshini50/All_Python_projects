class Levell1:
    variable_1 = 100

    def __init__(self):
        self.var_1 = 101  # Instance variable

    def fun_1(self):
        return 102

    def fun_name(self):
        return "Level 1"


class Levell2(Levell1):
    variable_2 = 200

    def __init__(self):
        super().__init__()
        self.var_2 = 201

    def fun_2(self):
        return 203

    # Override method
    def fun_name(self):
        return "Level 2"

class Levell3(Levell2):
    variable_3 = 300

    def __init__(self):
        super().__init__()
        self.var_3 = 301

    def fun_3(self):
        return 303

    # Override method
    #def fun_name(self):
        #return "Level 3"


obj = Levell3()
obj_1 = Levell1()
print(obj.variable_1, obj.var_1, obj.fun_1())
print(obj.variable_2, obj.var_2, obj.fun_2())
print(obj.variable_3, obj.var_3, obj.fun_3())
# Check the subclasses
print(issubclass(Levell3, Levell1))
print(issubclass(Levell2,Levell1))
print(issubclass(Levell3, Levell2))
# Instance of a class
print(isinstance(obj, Levell3))
print(isinstance(obj, Levell2))
print(isinstance(obj, Levell1))
print(isinstance(obj_1, Levell2))
print(isinstance(obj_1, Levell3))
# Access the override method
#print(obj.fun_name())  # Access the method of object property
print(obj.fun_name())  #  Access the method of superclass from bottom to top
print(obj_1.fun_name())
