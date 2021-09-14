class SuperClass:
    pass


class Classy(SuperClass):
    pub_var = 10  # public class variable
    __pri_var = 'Private class variable'  # private class variable

    def __init__(self, value=None):  # Constructor which contains the Instance variable of the object
        self.var = value  # public instance variable

    def visible(self):  # public method and can be invoked through the object
        self.__name = 'Private Attribute'  # private instance variable
        print('Visible')

    def __hidden(self):  # private method
        self.__attr = 'Private Attr2'  # private instance variable
        print('Hidden')


obj_1 = Classy("object")
obj_2 = Classy()

# Check the attributes of the objects
print(obj_1.__dict__)
print(obj_2.__dict__)

# Call the different methods in the class
obj_1.visible()
obj_1._Classy__hidden()  # private method invocation

# Check the properties(__dict__ contains only instance variables)
print(obj_1.__dict__)

# Directly access the properties/attributes
print(obj_1.var)
print(obj_2.var)
print(obj_1._Classy__attr)  # access the private property

# To access the class variable
print(obj_1.pub_var)
print(obj_1._Classy__pri_var)
print(obj_2.pub_var)
print(obj_2._Classy__pri_var)

# Check object/class contains Attribute
print(hasattr(obj_1, 'var'))  # public instance variable
print(hasattr(obj_1, 'pub_var'))  # public class variable
print(hasattr(obj_1, '_Classy__pri_var'))  # private class variable
print(hasattr(obj_1, '_Classy__name'))  # private instance variable

# Check different properties of class
print(Classy.__name__)
print(Classy.__dict__)
print(Classy.__module__)
print(obj_1.__module__)
print(Classy.__bases__)
print('_Classy__hidden' in Classy.__dict__.keys())
