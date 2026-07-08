class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_iterative(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

def reverse_recursive(head):
    if not head or not head.next:
        return head
    new_head = reverse_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head

# Khởi tạo: 1 -> 2 -> 3
h1 = Node(1, Node(2, Node(3)))
h1 = reverse_iterative(h1)
print(h1.val, h1.next.val, h1.next.next.val)