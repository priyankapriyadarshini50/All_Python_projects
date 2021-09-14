class ExampleClass:
    counter = 0  # class variable
    __count = 0  # private class variable

    def __init__(self, val=1):
        self.first = val
        ExampleClass.counter += 1
        ExampleClass.__count += 2


example_object_1 = ExampleClass()
example_object_1.__second = 5 # private instance variable outside the class
print(example_object_1.__dict__, example_object_1.counter)
print(example_object_1._ExampleClass__count)  # Accessing the private class variable using mangling
print(example_object_1.__second)  # does not need name mangling for private instance variable declared outside class

example_object_2 = ExampleClass(2)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_2._ExampleClass__count)

example_object_3 = ExampleClass(3)
print(example_object_3.__dict__, example_object_3.counter)
print(example_object_3._ExampleClass__count)
print(ExampleClass.__dict__)
print()


class ExampleClass1:
    varia = 1

    def __init__(self, val):
        self.varia = val  # Instance Variable
        ExampleClass1.varia = val  # Changing the class variable value

    def get_value(self, val):
        self.varia += val  # Changing the instance variable value


print(ExampleClass1.__dict__)
example_object = ExampleClass1(2)
example_object.get_value(4)

print(ExampleClass1.__dict__)
print(example_object.__dict__)
print()


class ExampleClass3:
    a = 1

    def __init__(self, val):
        if val % 2 != 0:
            self.b = 2
        else:
            self.c = val


exam_object = ExampleClass3(1)

print(hasattr(exam_object, 'b'))
print(hasattr(exam_object, 'a'))
print(hasattr(exam_object, 'c'))
print(hasattr(ExampleClass3, 'b'))
print(hasattr(ExampleClass3, 'a'))
