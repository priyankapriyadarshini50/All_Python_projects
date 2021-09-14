class A:
    top = 1

    def __init__(self):
        self.val = 1


class B(A):
    mid = 2

    def __init__(self):
        super().__init__()
        self.val = 2
        self.__val = 3


class C(B, A):
    bottom = 3

    def __init__(self):
        A.__init__(self)  # if we remove class A init(), then obj_c will access class B val=2
        B.__init__(self)  # if we remove class B init(), then obj_c will access class A val=1


obj_a = A()
obj_b = B()
obj_c = C()
print(obj_c.val)
print("----------------------")


class ExampleClass:
    counter = 0

    def __init__(self, val=4):
        self.__first = val
        ExampleClass.counter += 1


obj_1 = ExampleClass()
obj_2 = ExampleClass(2)
print(obj_1.counter)
print(obj_1._ExampleClass__first)
print(obj_2.counter, obj_2._ExampleClass__first)
print("--------------------------")


class Complex:
    def __init__(self, real, image):
        self.real = real
        self.image = image

    def __str__(self):
        return f"{self.real}+i{self.image}"

    def __repr__(self):
        return f"The complex number:{self.real}+i{self.image}"


com = Complex(10, 20)
print(com)
print(com.__repr__())


# TO ACCESS CLASS VARIABLES, DO NOT NEED INIT() METHOD
class Super:
    supVar = 1


class Sub(Super):
    subVar = 2


sub = Sub()
print(sub.supVar)
print(sub.subVar)
print("---------------------")


# TO ACCESS INSTANCE VARIABLES, WE HAVE TO USE THE INIT() OF SUPER CLASS IN SUBCLASS INIT()
class Super1:
    def __init__(self):
        self.sup_var = 4


class Sub1(Super1):
    def __init__(self):
        super().__init__()
        self.sub_var = 5


sub1 = Sub1()
print(sub1.sub_var)
print(sub1.sup_var)


# STR() SUPERSEDE THE ARGUMENT PRESENT WHILE ERROR RAISED
class Err(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)
        self.msg = msg

    def __str__(self):
        return f"From error block"


try:
    print("Start")
    raise Err("Error raised")
except Err as e:
    print(e)
except Exception as e1:
    print(e1)
else:
    print("From else block")
finally:
    print("From finally block")
print("\n")


class Mouse:
    Population = 0

    def __init__(self, name):
        Mouse.Population += 1
        self.name = name

    def __str__(self):
        return "Hi, my name is " + self.name


class LabMouse(Mouse):
    def __init__(self, name):
        Mouse.__init__(self, name)
        #self.name = name


professor_mouse = LabMouse("Professor Mouse")
print(professor_mouse, Mouse.Population)
print()


class A1:
    def __init__(self):
        self.a = 10


class B1(A1):
    pass


b1 = B1()
print(b1.__dict__)


class A2:
    def __init__(self):
        self.a = 10


class B2(A2):
    def __init__(self):
        A2.__init__(self)  # if i will not call, then b2 will not access instance variable a
        self.b = 20


b2 = B2()
print(b2.__dict__)


class A10:
    def do(self):
        print("A")


class BL(A10):
    def do(self):
        print("BL")


class BR(A10):
    pass
    # def do(self):
        #print("BR")


class C10(BR, BL):
    pass


o = C10()
o.do()


class Top:
    pass


class Left(Top):
    def say(self):
        print("Left")


class Right(Top):
    def say(self):
        print("Right")


class RightMost:
    pass


class Bottom(Left, Right, RightMost):
    pass


b = Bottom()
print(Bottom.__bases__)
print(Right.__bases__)
print(Bottom.__module__)
print(b.__module__)
print(Top.__bases__)
print()


class Un:
    value = 'Ein'

    def say(self):
        return self.value.lower()


class Duex(Un):
    value = 'Zwei'


class Trio(Un):
    def say(self):
        return self.value.upper()


class Quatre(Trio, Duex):
    pass


d = Quatre()
b = Duex()
print(isinstance(d, Un))
print(d.say() == 'ZWEI')
print(Trio in Quatre.__bases__)
# print(d.__name__) # AttributeError
print(type(d).__name__)
print(Quatre.__name__)




