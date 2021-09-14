two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y

for a in range(-2, 3):
    print(sqr(a))
    print(pwr(a, two()))
# Lambda expression and map() function
list_1 = [x for x in range(5)]
gen_1 = map(lambda x: x ** 2, list_1)
print(list_1)
print(gen_1)
# Convert the generator to a list
list_2 = list(gen_1)

for item in map(lambda y: 2 ** y, list_2):
    print(item, end=',')
print('\n')
# LAMBDA FUNCTION USING 2 ARGUMENTS LIST
for val in map(lambda x, y: x ** y, [m for m in range(1, 5)], [n for n in range(2, 6)]):
    print(val)
print("----------------------")


# Lambda Expression and filter() function
from random import randint, seed
data = [randint(-10, 10) for i in range(5)]
print(data)
# if the lambda expression
for v in filter(lambda x: x > 0 and x%2 == 0, data ):
    print(v, end=',')

for add_value in map(lambda x: x+x, [i for i in range(5)]):
    print("The addition result: ", add_value, end=',',)

