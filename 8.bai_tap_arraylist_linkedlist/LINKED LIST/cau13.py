def merge(a, b):
    if not a:
        return b

    if not b:
        return a

    if a.data < b.data:
        a.next = merge(a.next, b)
        return a

    b.next = merge(a, b.next)
    return b


def mergeSort(head):
    if not head or not head.next:
        return head

    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None

    left = mergeSort(head)
    right = mergeSort(mid)

    return merge(left, right)