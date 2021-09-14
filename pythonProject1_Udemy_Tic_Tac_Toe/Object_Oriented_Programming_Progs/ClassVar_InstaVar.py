class ExampleClass:
    item = 1  # Class variable

    def __init__(self, val):
        self.num = val  # num is the instance variable
        ExampleClass.item = val  # Assigning value to the class variable


print(ExampleClass.__dict__)
example_object = ExampleClass(2)


print(ExampleClass.__dict__)
print(example_object.__dict__)
# Access the class variable
print(ExampleClass.item)
# Access the instance variable
print(example_object.num)


class Circle:

    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * Circle.pi * self.radius


my_circle = Circle(5)
print(my_circle.circumference())


# the difference between these two __dict__ variables, the one from the class and the one from the object.
class SampleClass:
    varia = 5  # Class variable

    def __init__(self, val):  # Constructor
        SampleClass.varia = val  # value assigned to class variable

    def display(self, num):
        self.varia = num  # instance variable is reassigned


print(SampleClass.__dict__)
sample_object = SampleClass(3)
sample_object.display(7)
print(sample_object.varia)
sample_object.varia += 1
print(sample_object.varia)

print(SampleClass.__dict__)  # class variable value changed as val is assigned to it
print(sample_object.__dict__)  # No instance variable for the object

