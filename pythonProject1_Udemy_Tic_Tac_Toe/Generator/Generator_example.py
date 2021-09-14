def create_cubes(n):
    result = []
    for i in range(n):
        result.append(i**3)
    return result


# it creates a list of numbers which store in the memory
print(create_cubes(10))


# Instead of a list we can create a generator using yield
def create_cubes_gen(n):
    for i in range(n):
        yield i**3


#for i in range(5):
    #print(create_cubes_gen(10).__next__())
print(create_cubes_gen(10))

for num in create_cubes_gen(10):
    print(num, end=' ')

