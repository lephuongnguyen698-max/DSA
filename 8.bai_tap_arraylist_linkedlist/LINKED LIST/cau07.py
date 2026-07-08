class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def pushBack(self, x):
        node = Node(x)

        if not self.head:
            self.head = node
            return

        cur = self.head
        while cur.next:
            cur = cur.next

        cur.next = node

    def middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data


ll = LinkedList()

for x in [1, 2, 3, 4, 5]:
    ll.pushBack(x)

print(ll.middle())