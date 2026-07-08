class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def removeKthFromEnd(self, k):
        dummy = Node(0)
        dummy.next = self.head

        fast = dummy
        slow = dummy

        for _ in range(k):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        self.head = dummy.next