class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def pushBack(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
            return

        cur = self.head
        while cur.next:
            cur = cur.next

        cur.next = node

    def remove(self, x):
        if self.head and self.head.data == x:
            self.head = self.head.next
            return

        cur = self.head

        while cur and cur.next:
            if cur.next.data == x:
                cur.next = cur.next.next
                return
            cur = cur.next

    def printList(self):
        cur = self.head
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("null")


ll = LinkedList()

for x in [1, 2, 3, 2]:
    ll.pushBack(x)

ll.remove(2)
ll.printList()