def outer(par):
    loc = par

    def inner():
        return loc
    return inner


var = 10
# The outer function returns a copy of the inner() function
# so fun function is called a closure
fun = outer(var)
print(fun())


# Closure function with a parameter
def outer_1(p):
    x = p

    def inner_1(y):
        return y ** x
    return inner_1


sqr = outer_1(2)
cub = outer_1(3)

sqr_list = [sqr(i) for i in range(5)]
cub_list = [cub(i) for i in range(5)]
print(sqr_list)
print(cub_list)
