class WeekDayError(Exception):
    pass


class Weeker:
    __names = ['Mon', 'Thu', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        try:
            self.__current = Weeker.__names.index(day)
        except ValueError:
            raise WeekDayError

    def __str__(self):
        return Weeker.__names[self.__current]

    def add_days(self, n):
        self.__current = (self.__current + n) % 7

    def subtract_days(self, n):
        self.__current = (self.__current - n) % 7


try:
    weekday_obj = Weeker('Mon')
    print(weekday_obj)
    weekday_obj.add_days(15)
    print(weekday_obj)
    weekday_obj.subtract_days(23)
    print(weekday_obj)
    weekday_obj1 = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
