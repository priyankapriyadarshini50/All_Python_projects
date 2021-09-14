class Classy:
    def __init__(self):
        self.val = 2

    def method(self):
        print('Method')

    def __hidden(self):
        print('Hidden')


obj_1 = Classy()
print(obj_1.__dict__)  # Object can access the dict attribute
print(Classy.__dict__)  # Class can access the dict attribute
print(Classy.__name__)  # built in class attribute
#  to find the class of a particular object
print(type(obj_1))
print(type(obj_1).__name__)
# To find the name of the module
print(obj_1.__module__)
print(Classy.__module__)
