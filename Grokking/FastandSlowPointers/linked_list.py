from linked_list_node import LinkedListNode


# Template for the linked list
class LinkedList:
    # __init__ will be used to make a LinkedList type object.
    def __init__(self):
        self.head = None # Indicates empty list

    # Inserts a LinkedListNode at head of a linked list.
    def insert_node_at_head(self, node):
        if self.head:   # Checks if LL has a head node
            node.next = self.head # Ensures new node points to current head
            self.head = node # Updated to point to the new node
        else:
            self.head = node # If LL is empty, node becomes new head directly

    # Creates the linked list using the given integer array with the help of
    # InsertAthead method.
    def create_linked_list(self, lst):
        for x in reversed(lst):     # Iterates through elements of 'lst' in reverse order
            new_node = LinkedListNode(x) # For each element x, it creates a new LinkedListNode object 'new_node' with 'x' as data value
            self.insert_node_at_head(new_node) # Inserts new_node at head of LL

    # returns the number of nodes in the linked list
    def get_length(self, head):
        temp = head
        length = 0
        while(temp): # Iterates until Temo becomes None
            length+=1
            temp = temp.next
        return length

    # returns the node at the specified position(index) of the linked list
    def get_node(self, head, pos):
        if pos != -1: # If the position is valid
            p = 0 # Current position
            ptr = head # Pointer at first node
            while p < pos: # While current position is not desired position
                ptr = ptr.next # Update pointer to next node
                p += 1 # Current position + 1
            return ptr

    # __str__(self) method will display the elements of linked list.
    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next
            if temp:
                result += ", "
        result += ""
        return result
