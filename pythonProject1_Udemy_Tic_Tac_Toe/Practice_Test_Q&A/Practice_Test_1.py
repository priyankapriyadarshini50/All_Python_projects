m = 0


def foo(n):
    global m
    assert m != 0
    try:
        return 1/n
    except ArithmeticError:
        raise ValueError


try:
    foo(0)
except ArithmeticError:
    m += 2
except:
    m += 1
print(m)
print("------------------------")


class MyClass:
    variable = 10

    def __init__(self):
        self.value = 0


obj_1 = MyClass()
obj_1.variable += 1  # here variable is a newly created instance variable whoose value is class variable + 1(10+1)
print(obj_1.variable)
print(hasattr(obj_1, "variable"))
print(obj_1.__dict__)
obj_2 = MyClass()
obj_2.value += 1
print(obj_2.value)
print(hasattr(obj_2, "value"))
print(obj_2.variable + obj_1.value)
print('----------------------------')
print(str(1-1) in "012345£739"[:2])
print(10 << 2)  # 10 * 2 ** 2
print(17 >> 1)  # 17//(2 ** 1)
print("\n")
n = 1
while n < 5:
    print(n)
    n += 1
else:
    print("The while loop ended and else block executed.")
print("\n")

n1 = 1
while n1 < 5:
    print(n1)
    n1 += 1
    if n1 == 3:
        break
else:
    print("else block executed after break statement.")
print("\n")

n2 = 1
while n2 < 5:

    n2 += 1
    if n2 == 3:
        continue
    print(n2)
else:
    print("else block executed after the completion of while loop.")
print("\n")

i = 8
for i in range(10):
    print(i, end=" ")
else:
    print("Else block executed after the for loop completion.")
    print(i)

# SCOPE OF THE VARIABLES
var = 1


def my_fun():
    var1 = 2
    print("The variables are: ", var1, var)
    var1 += 1
    # var += 2 can't modify variable defined outside the function
    print("The changed values are: ", var1, var)


my_fun()
var += 4  # can modify outside the function
print(var)


# CLASS QUESTION
class A:
    def a(self):
        print("A", end="")

    def b(self):
        self.a()


class B(A):
    def a(self):
        print("B", end='')

    def do(self):
        self.b()


class C(A):
    def a(self):
        print("C", end='')

    def do(self):
        self.b()


B().do()
C().do()
print("\n")

my_tuple = (1, 2, 3, 4)
print("The value is: ", my_tuple[2])
print("\n")

x = 30
y = 45


def sun_fun(x):
    #global x
    print("the sum is ", x+y)


sun_fun(25)

print("%.2o" % 25)


class Calculate:
    A = 20
    B = 20

    def __init__(self,a,b):
        self.A = a
        self.B = b
        print(self.A + self.B/2 + 1)


cal = Calculate(5, 6)
print("\n")
a = 0
b = a ** 0
print(a, b)
print("20" > "30")
print("\n")

lst_1 = [i//i for i in range(1, 4)]
print(lst_1)
sum = 0
for n in lst_1:
    sum += n
print(sum)

lst = [[c for c in range(r)] for r in range(3)]
print(lst)
for x in lst:
    for y in x:
        print(y)
        if y < 2:
            print("*")

print("\n")
from math import * # WRONG, ONLY IMPORT WOULD WORK
# print(dir(math.sqrt))

# import math as mat
# print(dir(mat))

s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
s3 = sorted(s2)
print(s3)
print(s3[1])
print()


class Classy:
    var = 1

    def __init__(self):
        self.prop = 1


o = Classy()
o.var += 1
print(o.var, Classy.var)
print(Classy.var + o.prop)
print()


class A:
    def __init__(self):
        self.var = 10


class B(A):
    var = 1


class C(A):
    var = 2


class D(B, C):
    pass


d = D()
print(d.var)  # accessing the instance variable
print(d.__dict__)
print("\n")


class Team:
    def show_ID(self):
        return self.get_ID()

    def get_ID(self):
        return "anonymous"


class A(Team):
    def get_ID(self):
        return "Alpha"


a = A()
print(a.show_ID())
print()

import sys
print(sys.path)

import os
print(os.getcwd())
print(os.listdir('C:\\Users\\umesh\\PycharmProjects\\pythonProject1_Udemy_Tic_Tac_Toe\\Lambda_Expression'))

import math
print(dir(math))

print("my name is 'Priyanka'")
print('My name is "Priyanka"')
print('''This is a "Single line" string''')
print("This a '''Multi line''' string")
print("\a")
print(len("string"))
print("string"[2:100])
print(len("string"[2:100]))
print("string"[-100:-200])
print(len("string"[-100:-200]))
print('Alpha' <= 'alpha')
# print(100 <= '100')  # shows TypeError

import math
try:
    print(math.pow(2))
except ValueError:
    print('B')
except TypeError:
    print('A')
else:
    print('C')
print()

source = [1, 2, 4, 8, 16]
target = [x // 2 for x in source if x < 10]
print(target)
print(target[1])


