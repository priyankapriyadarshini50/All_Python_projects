def read_int(prompt, min, max):
    do_it = False
    while not do_it:
        try:
            val = int(input(prompt))
            assert min < val < max, "The entered value is not within the range!"
            do_it = True

        except ValueError as ex:
            print(ex)
            print("Error: wrong input")

        except AssertionError as ae:
            print(ae)
            # print(f"Error: the value is not within permitted range( {min}..{max} )")
    return val


v = read_int("Enter a number from -10 to 10: ", -10, 10)
print("The number is:", v)


def div(n):
    try:
        assert n != 0, "Any number is not divisible by zero"
        return 1/n
    except ZeroDivisionError as e:
        print(e)
    except AssertionError as a:
        print(a)


print(div(1))
print(div(0))
