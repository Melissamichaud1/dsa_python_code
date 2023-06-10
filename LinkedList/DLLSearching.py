class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    # Creation
    def createDLL(self, nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "The doubly linked list is created"

    # Insertion
    def insertNode(self, nodeValue, location):
        if self.head is None:
            print("The node cannot be inserted")
        else:
            newNode = Node(nodeValue)
            if location == 0: # Beginning
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == 1: # End
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else: # Middle
                tempNode = self.head
                index = 0
                while index < location - 1: # traverse
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode # reverse link
                newNode.next.prev = newNode # reverse link
                tempNode.next = newNode
    # Traversal
    def traverseDLL(self):
        if self.head is None:
            print("There are no elements to traverse")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
    # Reverse Traversal
    def reverseTraversalDLL(self):
        if self.head is None:
            print("There are no elements to traverse.")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev
    # Searching
    def searchDLL(self, nodeValue):
        if self.head is None:
            return "There are no elements in the list"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
            return "The node does not exist in this list"


# Create
doublyLL = DoublyLinkedList()
doublyLL.createDLL(5)

print([node.value for node in doublyLL])

# Insertion
doublyLL.insertNode(0,0)
doublyLL.insertNode(2,1)
doublyLL.insertNode(6,2)

print([node.value for node in doublyLL])

# Traversal
doublyLL.traverseDLL()

# Reverse Traversal
doublyLL.reverseTraversalDLL()

# Searching
print(doublyLL.searchDLL(6))
