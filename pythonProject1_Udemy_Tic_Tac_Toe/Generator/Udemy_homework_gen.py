def gen_squares(N):
    for i in range(N):
        yield i**2


for num in gen_squares(10):
    print(num)


# PROBLEM: 2
import random


def rand_num(low, high, n):
    for i in range(n):
        yield random.randint(low, high)


for number in rand_num(1, 10, 12):
    print(number)


#PROBLEM: 3
s = 'hello'
itr_obj = iter(s)
print(itr_obj)
print(next(itr_obj))
print(next(itr_obj))
print(next(itr_obj))


# Problem 5
my_list = [1, 2, 3, 4, 5]
# generator comprehension
gencomp = (item for item in my_list if item > 3)

print(type(gencomp))
for item in gencomp:
    print(item)
