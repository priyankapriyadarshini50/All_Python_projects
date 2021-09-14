class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self,val):
        self.__stack_list.append(val)

    def pop(self):
        last_val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return last_val


class SummationStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0  # private attribute so noone can change the value

    #def push(self, val): Do not need to write push() again as the child object can access the parent methods
     #   Stack.push(self, val)

    def pop(self):
        last_val = Stack.pop(self)
        self.__sum += last_val

    def get_sum(self):
        return self.__sum


sumstack_object = SummationStack()
# Adding numbers to the stack
for i in range(10, 15):
    sumstack_object.push(i)
for i in range(10, 15):
    sumstack_object.pop()

print(sumstack_object.get_sum())

object1 = Stack()
object2 = Stack()
object3 = Stack()

object1.push(1)
print(object1._Stack__stack_list)

object2.push(object1.pop()+ 1)
print(object2._Stack__stack_list)

object3.push(object2.pop()-2)
print(object3._Stack__stack_list) # Accessing the private attribute/properties

print(object3.pop())

# Another better approach for the sum program: Solution2
class Stack1:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)
        return len(self.__stack_list)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


class AddingStack1(Stack1):
    def __init__(self):
        Stack1.__init__(self)
        self.__sum = 0

    def stack_sum(self, num):

        for j in range(num):
            last_val = add_stack_obj.pop()
            self.__sum += last_val
        return self.__sum


add_stack_obj = AddingStack1()

for i in range(10):
    num = add_stack_obj.push(i)
print(num)

print(add_stack_obj.stack_sum(num))



