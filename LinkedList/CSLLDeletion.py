class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
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

    # Creation
    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "The CSLL has been created"

    # Insertion
    def insertCSLL(self, value, location):
        if self.head is None:
            return "The head reference is None"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return "The node has been successfully inserted"
    # Traversal
    def traverseCSLL(self):
        if self.head is None:
            print("There are no elements for traversal")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break

    # Searching
    def searchCSLL(self, nodeValue):
        if self.head is None:
            return "There are no nodes in this CSLL"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return "The node does not exist in this CSLL"

    # Deletion
    def deleteNode(self,location):
        if self.head is None:
            print("There are no nodes in this CSLL")
        else:
            if location == 0: # Delete from beginning
                if self.head == self.tail: # One node
                    self.head.next = None
                    self.head = None
                    self.tail = None # Deletes the node
                else: # More than one node
                    self.head = self.head.next # Access head's next reference, physical location of 2nd node
                    self.tail.next = self.head
            elif location == 1: # Delete from end
                if self.head == self.tail: # One node
                    self.head.next = None
                    self.head = None
                    self.tail = None # Deletes the node
                else: # More than one element
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next


# create CSLL -> [1]
circularSLL = CircularSinglyLinkedList()
circularSLL.createCSLL(1)

# add element to beginning
circularSLL.insertCSLL(0,0)
# add element to the end
circularSLL.insertCSLL(2,1)
# add element to the end
circularSLL.insertCSLL(3,1)
# add element in the middle
circularSLL.insertCSLL(2,2)
print([node.value for node in circularSLL])

# traverse
# circularSLL.traverseCSLL()

# # searching
# print(circularSLL.searchCSLL(4))

# deletion
# delete from beginning
circularSLL.deleteNode(0)


print([node.value for node in circularSLL])
