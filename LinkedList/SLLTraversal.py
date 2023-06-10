# Traversal

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

# Traverse Singly Linked List
def traverseSLL(self):
    if self.head is None:
        print("The singly linked list does not exist")
    else:
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

singlyLinkedList = SLinkedList()
singlyLinkedList.traverseSLL()
