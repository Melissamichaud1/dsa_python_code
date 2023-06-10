class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)

    def enqueue(self, value):
        newNode = Node(value)
        if self.linkedList.head == None: # no elements in LL
            self.linkedList.head = newNode # inserting new node
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode # link between last node and new node
            self.linkedList.tail = newNode # add element to end of LL

    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False

    def dequeue(self):
        if self.isEmpty():
            return "There are no nodes in the queue"
        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail: # checks if there is more than 1 node
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next # create link between head and 2nd node, 1st node can be destroyed now
            return tempNode

    def peek(self): # returns first element of queue
        if self.isEmpty():
            return "There are no nodes in the queue"
        else:
            return self.linkedList.head

    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None


custQueue = Queue()
custQueue.enqueue(1)
custQueue.enqueue(2)
custQueue.enqueue(3)
print(custQueue) # 1 2 3
print(custQueue.dequeue()) # 1
print(custQueue) # 2 3
print(custQueue.peek()) # 2
