class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    # Creation of Circular Doubly Linked List
    def createCDLL(self, nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode
        return "The CDLL is created successfully"

    # Insertion Method in Circular Doubly Linked List
    def insertCDLL(self, value, location):
        if self.head is None:
            return "The CDLL does not exist"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
            return "The node has been successfully inserted"

    # Traversal of Circular Doubly Linked List
    def traversalCDLL(self):
        if self.head is None:
            print("There are no nodes for traversal")
        else:
            tempNode = self.head # start from first node
            while tempNode:
                print(tempNode.value)
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next

    # Reverse traversal of Circular Doubly Linked List
    def reverseTraversalCDLL(self):
        if self.head is None:
            print("There are no nodes for reverse traversal")
        else:
            tempNode = self.tail # start from last node
            while tempNode:
                print(tempNode.value)
                if tempNode == self.head:
                    break
                tempNode = tempNode.prev # traverse backward

    # Search Circular Doubly Linked List
    def searchCDLL(self, nodeValue): # value we are looking for
        if self.head is None:
            return "There are no nodes in CDLL"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                if tempNode == self.tail: # prevents infinite loop, stops at the last node
                    return "The value does not exist in the CDLL"
                tempNode = tempNode.next

circularDLL = CircularDoublyLinkedList()
circularDLL.createCDLL(5)
circularDLL.insertCDLL(0,0)
circularDLL.insertCDLL(1,1)
circularDLL.insertCDLL(2,2)
print([node.value for node in circularDLL])
# circularDLL.traversalCDLL()
# circularDLL.reverseTraversalCDLL()
print(circularDLL.searchCDLL(2))
