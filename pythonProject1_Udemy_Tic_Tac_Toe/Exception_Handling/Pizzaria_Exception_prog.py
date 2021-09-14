class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza


class TooMuchCheeseError(PizzaError):
    def __init__(self, cheese, pizza, message):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese


def make_pizza(pizza, cheese):
    if pizza not in ['margareta', 'calzone', 'capricciosa']:
        raise PizzaError(pizza, 'no such pizza on the menu')
    if cheese > 100:
        raise TooMuchCheeseError(cheese, pizza, "too much cheese")
    else:
        print('Pizza is Ready')


for pz, ch in [('mafia', 20), ('calzone', 0), ('margareta', 110), ('pepperoni', 115)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)
    else:
        print("The is perfect!!")
    finally:
        print('THE END')
