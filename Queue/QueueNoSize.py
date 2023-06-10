class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def enqueue(self, value):
        self.items.append(value)
        return "The element is inserted at the end of queue"

    def dequeue(self):
        if self.isEmpty():
            return "There are no elements in the queue"
        else:
            return self.items.pop(0) # removes first element

    def peek(self):
        if self.isEmpty():
            return "There are no elements in the queue"
        else:
            return self.items[0] # returns first element of the list

    def delete(self):
        self.items = None

customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.isEmpty()) # prints False
print(customQueue) # prints 1 2 3
print(customQueue.dequeue()) # prints 1
print(customQueue) # prints 2 3
print(customQueue.peek()) # prints 2 the first element
