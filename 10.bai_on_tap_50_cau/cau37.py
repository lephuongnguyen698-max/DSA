def find_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# Khởi tạo: 1 -> 2 -> 3 -> 4 -> 5
h2 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
mid = find_middle(h2)
print(mid.val)