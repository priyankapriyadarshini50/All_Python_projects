import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return point1.__x, point2.__x

    def gety(self):
        return point1.__y, point2.__y

    def distance_from_xy(self, x, y):
        d = ((self.__x - x) ** 2 + (self.__y - y) ** 2) ** 0.5
        return d

    def distance_from_point(self, point):
        x1, x2 = point.getx()
        y1, y2 = point.gety()
        dis = ((x2-x1) ** 2 + (y2-y1) ** 2) ** 0.5
        # or
        # self.distance_from_xy(point.getx(), point.gety())
        return dis


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))


# Solution#2
import math


class Point:
    def __init__(self, x=0.0, y=0.0):
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


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
