import math

from math import ceil, floor, trunc, factorial, hypot

x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))
print(factorial(4.000))  # it will not create ValueError, show deprecation Warning
#print(factorial(-2))  # create ValueError

print(hypot(x, y))
print(math.floor(3.45))  # x <= x
print(math.ceil(3.45))
# ROUNDING A NUMBER
print("The round value:", round(3.45))  # round is a built-in function, does not belong to math module
print(round(3.456, 2))  # it will round up-to two decimal point
print(round(3.65, 0))

# CONSTANCE
print(math.pi)
print(math.e)
# print(math.inf)
print(math.nan)
print(math.tau)

# LOGARITHMIC VALUE
print(math.log(math.e))
from math import log, e
print(log(e))  # e**x == e, x=1.0
print(log(100, 10))  # 10 ** x == 100, x = 2.0
print(log(10))  # log value 10 with base e. e**x == 10
print(math.exp(2))  # e ** 2

# TRIGONOMETRY
from math import sin, radians, degrees, pi
print(sin(10))
print('Radian value: ', radians(180))
print('Degree: ', degrees(pi/2))
print(math.sin(90.0))

# TO GET THE SAME SET/SERIES OF RANDOM VALUES(mostly use for testing purpose)
import random

# random function 0.0 <= x <= 1.0
for i in range(5):
    print("The random fun include 0.0 and 1.0:", random.random())

random.seed(0)
for i in range(5):
    print(random.randint(0, 100))

# GET A RANDOM OF NUMBER FROM A GIVEN SET OF INTEGERS
my_list = list(range(0, 20))
print(my_list)
for j in range(10):
    print(random.choice(my_list), end=' ')
print()

# SELECT A SET OF RANDOM NUMBERS FROM A GIVEN LIST WITH REPEATED VALUES
print(random.choices(population=my_list, k=10))

# SELECT A SET OF RANDOM NUMBERS FROM A GIVEN LIST WITH UNIQUE VALUES
print(random.sample(population=my_list, k=10))

#
for i in range(5):
    print(random.randrange(10, 20, 2))

