class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def bubble_sort_linked_list(head):
    if head is None:
        return head

    swapped = True

    while swapped:
        swapped = False
        current = head

        while current.next:
            if current.value > current.next.value:
                current.value, current.next.value = current.next.value, current.value
                swapped = True

            current = current.next

    return head


def print_list(head):
    while head:
        print(head.value, end=" -> ")
        head = head.next
    print("null")


# Tạo danh sách: 1 -> 3 -> 2
head = Node(1)
head.next = Node(3)
head.next.next = Node(2)

head = bubble_sort_linked_list(head)

print_list(head)