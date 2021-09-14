class Stack:
    def __init__(self):
        self.__stack_list = []  # its a private attribute and it can't be access

    def push(self, val):
        self.__stack_list.append(val)  # As the list is a private, we can't print or see any values in this list

    def pop(self):
        last_val = self.__stack_list[-1]
        del self.__stack_list[-1]  # remove the last element of the list
        return last_val


stack_object = Stack()

for i in range(5):
    stack_object.push(i)

for i in range(5):
    print(stack_object.pop())
