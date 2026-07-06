class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge(a, b):
    dummy = Node(0)
    tail = dummy

    while a and b:
        if a.data < b.data:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next

        tail = tail.next

    if a:
        tail.next = a

    if b:
        tail.next = b

    return dummy.next