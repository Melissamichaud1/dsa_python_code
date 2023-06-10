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


# Search
singlyLinkedList = SLinkedList()
print(singlyLinkedList.searchSLL(3))
print(singlyLinkedList.searchSLL(33))
