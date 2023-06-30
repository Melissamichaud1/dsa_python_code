"""
Check whether or not a linked list
contains a cycle. If a cycle exists,
return TRUE. Otherwise, return FALSE.
The cycle means that at least one node
can be reached again by traversing the
next pointer.
"""
# TC = O(n) -> n number of nodes in LL
# SC = O(1)

from linked_list import LinkedList
from linked_list_node import LinkedListNode

def detect_cycle(head):
   if not head or not head.next:
      return False # No cycle if LL empty or 1 node
   slow = head
   fast = head
   while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

      if fast == slow:
         return True # Cycle detected

   return False # No cycle detected

# Example usage:
# Create linked list with a cycle:
linked_list = LinkedList()
node1 = LinkedListNode(1)
node2 = LinkedListNode(2)
node3 = LinkedListNode(3)
node4 = LinkedListNode(4)
node5 = LinkedListNode(5)

linked_list.head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2 # Create a cycle

solution = detect_cycle(linked_list.head)
print(solution)
