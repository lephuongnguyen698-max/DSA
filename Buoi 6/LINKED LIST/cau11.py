class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def pushFront(self, x):
        node = Node(x)

        if not self.head:
            self.head = self.tail = node
            return

        node.next = self.head
        self.head.prev = node
        self.head = node

    def pushBack(self, x):
        node = Node(x)

        if not self.tail:
            self.head = self.tail = node
            return

        self.tail.next = node
        node.prev = self.tail
        self.tail = node