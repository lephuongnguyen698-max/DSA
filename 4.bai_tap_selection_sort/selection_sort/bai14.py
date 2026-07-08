class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def sap_xep_danh_sach_lien_ket(head):

    current = head

    while current:

        min_node = current
        temp = current.next

        while temp:

            if temp.data < min_node.data:
                min_node = temp

            temp = temp.next

        current.data, min_node.data = min_node.data, current.data

        current = current.next

    return head