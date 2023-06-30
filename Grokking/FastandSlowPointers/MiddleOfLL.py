"""
Given the head of a singly linked list, return the middle node of the linked list.
If the number of nodes in the linked list is even, there will be two middle nodes,
so return the second one.
"""
# TC = O(n)
# SC = O(1)

from linked_list import LinkedList


def get_middle_node(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# Create a LL with odd number of nodes
linked_list_odd = LinkedList()
linked_list_odd.create_linked_list([1,2,3,4,5])

# test get_middle_node on the LL with odd number of nodes
middle_node_odd = get_middle_node(linked_list_odd.head)
print(middle_node_odd.data) # Output: 3

# Create a LL with even number of nodes
linked_list_even = LinkedList()
linked_list_even.create_linked_list([1,2,3,4,5,6])

# test get_middle_node on the LL with even number of nodes
middle_node_even = get_middle_node(linked_list_even.head)
print(middle_node_even.data) # Output: 4
