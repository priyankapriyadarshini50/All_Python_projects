import math


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(abs(self.__x - x), abs(self.__y - y))

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.vertice1 = vertice1
        self.vertice2 = vertice2
        self.vertice3 = vertice3

    def perimeter(self):
        a = self.vertice1.distance_from_point(self.vertice2)
        b = self.vertice2.distance_from_point(self.vertice3)
        c = self.vertice3.distance_from_point(self.vertice1)
        return a+b+c


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())


# Another Example of object as argument using the self keyword
class Foo:
    def __init__(self):
        self.values = [2, 4, 6, 9]

    def do_something(self, x, y):
        z = self.values[x] * self.values[y]
        return z


class Bar:
    def __init__(self, fobject):
        self.fobject = fobject

    def do_something(self, a, b):
        res = self.fobject.do_something(a, b)
        return res


bar = Bar(Foo())
print(bar.do_something(1,2))
