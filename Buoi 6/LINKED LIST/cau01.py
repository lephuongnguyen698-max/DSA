class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def pushFront(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def pushBack(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = newNode

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")


ll = LinkedList()

ll.pushFront(2)
ll.pushBack(5)

ll.printList()