class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def chen_node(sorted_head, new_node):

    if sorted_head is None or sorted_head.data >= new_node.data:
        new_node.next = sorted_head
        return new_node

    current = sorted_head

    while current.next and current.next.data < new_node.data:
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return sorted_head


def sap_xep_danh_sach_lien_ket(head):

    sorted_head = None

    current = head

    while current:
        next_node = current.next
        sorted_head = chen_node(sorted_head, current)
        current = next_node

    return sorted_head