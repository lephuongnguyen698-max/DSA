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

    def search(self, value):
        temp = self.head
        index = 0

        while temp:
            if temp.data == value:
                return index
            temp = temp.next
            index += 1

        return -1

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")


ll = LinkedList()

ll.pushBack(1)
ll.pushBack(2)
ll.pushBack(3)

ll.printList()

x = int(input("Nhập giá trị cần tìm: "))
print("Vị trí:", ll.search(x))