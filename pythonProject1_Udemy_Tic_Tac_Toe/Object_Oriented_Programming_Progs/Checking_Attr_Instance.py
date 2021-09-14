class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 5


example_object = ExampleClass(10)
# hasattr returns True and False if any object has any instance
if hasattr(example_object, 'a'):
    print('a:', example_object.a)
else:
    print('b:', example_object.b)


class ExampleClass2:
    a = 1

    def __init__(self):
        self.b = 2


example_object2 = ExampleClass2()

print(hasattr(ExampleClass2, 'a'))  # Checks if a is an instance of Class
print(hasattr(ExampleClass2, 'b'))  # Checks if b is an instance of Class
print(hasattr(example_object2, 'a'))  # Checks if a is an instance of object/object attribute
print(hasattr(example_object2, 'b'))  # Checks if a is an instance of object/object attribute

