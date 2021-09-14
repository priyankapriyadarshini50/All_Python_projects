class MyZeroDivisionError(ZeroDivisionError):
    pass


def do_the_division(mine):
    if mine:
        raise MyZeroDivisionError  # exception object is created with NO argument
    else:
        raise ZeroDivisionError("some bad news", "handled", "caught it")  # exception object is created with one argument


for mine in [False, True]:
    try:
        do_the_division(mine)
    except MyZeroDivisionError:
        print("User defined Error!")
    except ZeroDivisionError:
        print('Division by zero: built-in Error')


for val in [False, True]:
    try:
        do_the_division(val)
    except MyZeroDivisionError as e:
        print("My division by zero: User defined Error")
        print(e)  # display the property/argument of the exception object
        print(e.args)  # display the exception object args property which is a tuple with one argument
    except ZeroDivisionError as e:
        print('Division by zero')
        print(e)
        print(e.__str__())  # display the property(argument which passed ) of the exception object
        print(e.args)  # display the properties of the exception object in a tuple
