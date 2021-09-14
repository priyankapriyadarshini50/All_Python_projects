class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        last_val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return last_val


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__counter = 0

    def pop(self):
        Stack.pop(self)
        self.__counter += 1

    def get_counter(self):
        return self.__counter

counting_object = CountingStack()
for i in range(100):
    counting_object.push(i)
    counting_object.pop()
print(counting_object.get_counter())
