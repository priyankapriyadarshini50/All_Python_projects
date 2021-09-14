class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.line = []

    def put(self, elem):
        self.line.append(elem)

    def get(self):
        if len(self.line)> 0:
            first_entree = self.line[0]
            del self.line[0]
            return first_entree
        else:
            raise QueueError


class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)

    def isempty(self):
        if len(self.line) == 0:
            return True
        else:
            return False


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
