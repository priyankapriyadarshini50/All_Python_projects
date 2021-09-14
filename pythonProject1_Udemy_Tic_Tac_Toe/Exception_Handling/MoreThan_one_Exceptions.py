try:
    x = int(input('Enter a number: '))
    res = 1 / x
    print(res)

except ValueError as ve:
    print(ve)
    print('Please, enter an integer value.')
except ZeroDivisionError:
    print('Sorry, cannot be divisible by zero.')
except:
    print('Oops, Something went wrong!')

print('THE END')
#print('alpha'[1/0])

# KeyboardInterruptionError
# This code can not be terminated
# by pressing Ctrl C
#from time import sleep
#second = 0
#while True:
    #try:
        #print(second)
        #second += 1
        #sleep(1)
    #except KeyboardInterrupt:
        #print('Do not do that!')


# ImportError Exception
try:
    import time
    import math
    import abracadabra
except ImportError:
    print('One of the import has failed.')
print("\n")


# ASSERTION ERROR
def assertionTest(y):
    x = 1
    assert x/y, "Assertion argument"
    return x


try:
    assertionTest(0)
except AssertionError as ae:
    print(ae)
except ZeroDivisionError as ze:
    print(ze)
    print("A number is not divisible by zero!")
else:
    print("The result is: ", assertionTest(2))
finally:
    print("This is the final block")
print("\n")
# VALUE ERROR
try:
    val = int("10")  # it causes value error if 10.12
    res = val + '20'  # it causes type error
    print(val)
    print(res)

except ValueError as ve:
    print("Handled in ValueError block")
    print(ve)
except TypeError as te:
    print("Handled in TypeError block")
    print(te)
except Exception as e:
    print("Handles in Exception block")
    print(e)
else:
    print("No error occurred.")
finally:
    print("final block executed")


# INDEXERROR
the_list = [1, 2, 3, 4, 5]
ix = 0
do_it = True

while do_it:
    try:
        print(the_list[ix])
        ix += 1
    except IndexError as ie:
        print(ie)
        do_it = False

print('Done')
# KEYERROR
d = {'a': 'b', 'b': 'c', 'c': 'd'}
ch = 'a'
while True:
    try:
        ch = d[ch]
        print(ch)
    except KeyError:
        print("The key is not available in dictionary")
        break

# Assertion
var = 15
try:
    assert var == 0
    print(var)
except AssertionError as ae:
    print(ae)
    print("Assertion error occurred")
else:
    print("Else block")
#
try:
    print("5"/0)
except ArithmeticError:
    print("arith")
except ZeroDivisionError:
    print("zero")
except TypeError:
    print("Type")
except:
    print("some")

import math
try:
    print(math.pow(2, 3))
except TypeError:
    print('A')
else:
    print('B')
print(dir(math))


