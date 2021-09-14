import math as cal
print("Math function: ", cal.sin(cal.pi/2))
print(dir(cal))
var = 3.14
print(cal.ceil(var))  # Upper value
print(cal.floor(var))
print(cal.trunc(var))
print(round(var))


def sin(x):
    if x * 2 == 3.14:
        return 0.9999
    else:
        return None


pi = 3.14
print("User defined function: ", sin(pi/2))

any_list = [1, 2, 3, 4]
odd_list = list(map(lambda x:x%2,any_list))
print(odd_list)
odd_list1 = [x for x in any_list if x % 2]
print(odd_list1)
odd_list3 = list(filter(lambda x: x is 1 or x is 3, any_list))
print(odd_list3)  # even if it provides correct ans but it is showing SyntaxWarning
odd_list4 = list(filter(lambda x: x == 1 or x == 3, any_list))
print(odd_list4)

x = 5 % 3
y = x if x >= 1 else 4
print(x, y)

y1 = 0


def function(x, y1):
    #global y1
    y1 = 1
    assert y1 != 0
    try:
        return x/y1
    except ZeroDivisionError:
        raise ValueError


try:
    function(3, 0)
except ArithmeticError:
    y1 += 1
except:
    y1 += 3

print(y1)
print("---------------------------")
my_list = [1, 2, 3, 4]
try:
    x = my_list[4]
    print("The value of x: ", x)
except IndexError as e:
    print(e)
except LookupError as le:
    print(le)
print("-----------------")


number = '5'
try:
    # x = int("dog") # it raises ValueError
    # x = int(dog)  # it raises NameError
    y = 5 + 'dog'  # it raises TypeError
except ValueError as ve:
    x = 1
    print(ve)
    print(x)
except NameError as ne:
    x = 2
    print(ne)
    print(x)
except TypeError as te:
    x = 3
    print(te)
    print(x)

finally:
    print("The final block: ", number)
print("-----------------------------")


var = 1
def foo():
    global var
    var += 2

    def g():
        return var
    return g

a = foo()
#print(a())  # if a() is called here, the output 3
b = foo()
print(a, b)
print(a())  # here the output is 5
print(b())
print(a is b)
print(a() is b())
print(isinstance(a, type(foo)))

print("----------------------------")
b = bytearray(4)
print(b)
print("-----------------------")
my_tuple = (1, 2, 3, 4, 5, 6)
foo = list(filter(lambda x: x-0 and x-1, my_tuple))
print(foo)


