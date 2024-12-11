class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

head = ListNode(1, ListNode(2, ListNode(3)))
reversed_head = reverse_linked_list(head)
while reversed_head:
    print(reversed_head.value, end=" ")
    reversed_head = reversed_head.next
