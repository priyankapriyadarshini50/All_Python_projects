class A:
    def __init__(self, v=1):
        self.v = v

    def set(self, v):
        self.v = v
        return v


a = A()
print(a.set(a.v + 1))


# ________________________________
try:
    raise Exception(1, 2, 3)
except Exception as e:
    print(e)
    print(e.args)
    print(len(e.args))
print('-------------------------')


class Ex(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg + msg)
        self.args = (msg,)


try:
    raise Ex('ex')
except Exception as e1:
    print(e1)
    print(e1.args)
except Ex as e2:
    print(e2)


class A:
    X = 0

    def __init__(self, v=0):
        self.Y = v
        A.X += v


a = A()
b = A(1)
c = A(2)
print(c.X)


#________________________
def f(x):
    try:
        x = x/x
    except:
        print('a', end='')
    else:
        print('b', end='')
    finally:
        print('c', end='')


f(1)
f(0)
print("\n")


# ---------------------------
class A:
    def __init__(self, v):
        self.__a = v + 1

# a = A(0)
# print(a.__a)


# String slicing out of range is possible
st = "Hello"
s1 = st[-1:7]
print("s1:", s1)
s2 = st[0:7]
print("s2:", s2)
s3 = '\t'.join(["cat", "dog", "pig"])
s4 = '\\'.join(['cat', 'dog', 'pig'])
print(s3)
print(s4)


