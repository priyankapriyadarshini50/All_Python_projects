class SuperA:
    def __init__(self):
        self.var_a = 11

    def fun_name(self):
        return "SuperA"


class SuperB:
    def __init__(self):
        self.var_b = 21

    # Method Override
    def fun_name(self):
        return "SuperB"


class Sub(SuperB, SuperA):
    def __init__(self):
        SuperA.__init__(self)
        SuperB.__init__(self)


object_sub = Sub()
object_a = SuperA()
object_b = SuperB()

print(object_sub.var_a)
print(object_sub.var_b)

print(object_sub.fun_name())  # As in the same level, it accesses the method from left to right
