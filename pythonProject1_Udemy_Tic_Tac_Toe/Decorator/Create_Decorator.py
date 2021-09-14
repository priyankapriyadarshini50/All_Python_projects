def new_decorator(original_func):

    def wrap_func():
        print("The extra code is added before the original code.")
        original_func()
        print("The extra code is added after the original code.")
    return wrap_func


def func_needs_decorator():
    print("I am the original func and needs to be decorated.")


# Create a variable
#decorated_func = new_decorator(func_needs_decorator)
#decorated_func()
# now the new_decorator is working as a decorator
# instead of assigning the value as above, we can do like below
@new_decorator
def func_needs_decorator():
    print("I am the original func and needs to be decorated.")


func_needs_decorator()
