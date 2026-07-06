class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def pushBack(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = newNode

    def insertAfter(self, value, newValue):
        temp = self.head

        while temp:
            if temp.data == value:
                newNode = Node(newValue)
                newNode.next = temp.next
                temp.next = newNode
                return
            temp = temp.next

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")


ll = LinkedList()

ll.pushBack(1)
ll.pushBack(3)

print("Ban đầu:")
ll.printList()

ll.insertAfter(1, 2)

print("Sau khi chèn:")
ll.printList()