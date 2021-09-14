# Problem 1
try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except TypeError as te:
    print(te)
    print("** operator cannot be applied on strings!")
finally:
    print("The End!")


# Problem 2
x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print("Division by zero")
finally:
    print('All Done')


# Problem 3
def ask():
    while True:
        try:
            num = int(input('Enter a number: '))

        except ValueError:
            print('An error occurred! Please try again')
        else:
            print("Thank you! The square of the number is: ", num ** 2)
            break
        finally:
            print('The End')


ask()

