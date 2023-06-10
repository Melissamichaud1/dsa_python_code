class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # Inserting - SLL
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
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
                if tempNode == self.tail:
                    self.tail=newNode

    # Traversing - SLL
    def traverseSLL(self):
        if self.head is None:
            print("The singly linked list does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    # Searching - SLL
    def searchSLL(self, nodeValue):
        if self.head is None:
            return "The list does not exist."
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "The value does not exist in this list"

    # Delete a node - SLL
    def deleteNode(self, location):
        if self.head is None:
            print("The list does not exist.")
        else:
            if location == 0:   # Delete first node
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else: # More than 1 node in SLL
                    self.head = self.head.next # Change head reference to 2nd node
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else: # Traverse until we find node before last node, then updating nodes next reference to null, update tails reference
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None # Delete last node
                    self.tail = node # Change tail to reference previous node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    # Delete entire SLL
    def deleteEntireSLL(self):
        if self.head is None:
            print("The list does not exist.")
        else:
            self.head = None
            self.tail = None

# Insert
singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(1,1)
singlyLinkedList.insertSLL(2,1)
singlyLinkedList.insertSLL(3,1)
singlyLinkedList.insertSLL(4,1)
singlyLinkedList.insertSLL(0,0)
singlyLinkedList.insertSLL(0,3)

print([node.value for node in singlyLinkedList])

# Traverse
# singlyLinkedList.traverseSLL()

# Search
# print(singlyLinkedList.searchSLL(3))
# print(singlyLinkedList.searchSLL(33))

# Delete a node
# singlyLinkedList.deleteNode(3)
# print([node.value for node in singlyLinkedList])

# Delete entire SLL
singlyLinkedList.deleteEntireSLL()
print([node.value for node in singlyLinkedList])
