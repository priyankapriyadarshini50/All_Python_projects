def hello1(name='jose'):
    print("The hello function has been executed")

    def greet():
        return '\t This is greet function inside hello'

    def welcome():
        return '\t This is welcome function inside hello'
    # we can call these functions inside the hello function only
    print(greet())
    print(welcome())
    print('This is the end of hello function execution')


def hello2(name='jose'):
    print("The hello function has been executed")

    def greet():
        print("\t Hi, i am inside greet fun")

    def welcome():
        print("\t Hi, I am inside welcome fun")

    greet()
    welcome()
    print('This is the end of hello function execution')


hello1()
hello2()
# How we are going to access the functions (greet(), welcome()) outside hello()
# we have to return the greet() from hello()
def hello3(name='Jose'):
    print("The hello function has been executed")

    def greet():
        return '\t This is greet() function inside hello'

    def welcome():
        return '\t This is welcome() function inside hello'
    if name == 'Jose':
        return greet
    else:
        return welcome

# create an variable
my_new_fun = hello3('Jose')
print(my_new_fun())
# create another variable
my_new_fun2 = hello3("Priya")
print(my_new_fun2())


# Idea of creating a decorator
# create a function
def super_cool():
    # define another function inside it
    def cool():
        return 'I am cool!'
    return cool


# create a variable and assign that to the decorator(function call)
my_fun = super_cool()
print(my_fun())


# passing function as argument in a different function
def greet_hello():
    return 'Hello, I am Priyanka!'


def other_func(test_func):
    print("Other function code is going to execute")
    print(test_func())


other_func(greet_hello) # Only function name will pass as argument



