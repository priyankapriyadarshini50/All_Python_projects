#class QueueError(IndexError):
    #def __init__(self, msg):
        #IndexError.__init__(self, msg)
        #self.msg = msg


class Queue:
    def __init__(self):
        self.__line_list = []

    def put(self, elem):
        self.__line_list.append(elem)

    def get(self):
        if len(self.__line_list) > 0:
            first_elem = self.__line_list[0]
            del self.__line_list[0]
            return first_elem
        else:
            #raise QueueError("Empty stack")
            raise IndexError


que = Queue()
que.put(1)
que.put('dog')
que.put(False)
try:
    for i in range(5):
        print(que.get())
#except QueueError as qe:
    #print(qe)
    #print("Queue Error!")
except IndexError:
    print("Stack is empty and cause Index error.")

