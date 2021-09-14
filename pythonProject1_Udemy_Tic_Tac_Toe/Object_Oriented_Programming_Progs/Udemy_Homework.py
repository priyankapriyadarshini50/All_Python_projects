# Problem 1:
class Line:
    def __init__(self, coor1, coor2):
        self.x1, self.y1 = coor1
        self.x2, self.y2 = coor2

    def distance(self):
        return ((self.x2-self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5


    def slope(self):
        return (self.y2 - self.y1)/(self.x2 - self.x1)


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1,coordinate2)
print(li.x1, li.y1)
print(li.x2, li.y2)
# Calculate the distance
print(li.distance())
print(li.slope())


# Problem 2:
class Cylinder:
    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return Cylinder.pi * (self.radius ** 2) * self.height

    def surface_area(self):
        return 2 * Cylinder.pi * self.radius * (self.height + self.radius)


c = Cylinder(2, 3)
# Calculate the volume
print(c.volume())

# Calculate the area
print(c.surface_area())
