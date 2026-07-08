def split_list(head):
    slow = head
    fast = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    if prev:
        prev.next = None
    return head, slow

def merge_lists(l1, l2):
    dummy = Node(0)
    curr = dummy
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 if l1 else l2
    return dummy.next

def merge_sort_list(head):
    if not head or not head.next:
        return head
    left, right = split_list(head)
    left = merge_sort_list(left)
    right = merge_sort_list(right)
    return merge_lists(left, right)

# Khởi tạo: 3 -> 1 -> 2
h4 = Node(3, Node(1, Node(2)))
h4 = merge_sort_list(h4)
curr = h4
while curr:
    print(curr.val, end=" ")
    curr = curr.next
print()