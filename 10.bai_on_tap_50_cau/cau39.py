def remove_nth_from_end(head, k):
    dummy = Node(0, head)
    first = dummy
    second = dummy
    
    for _ in range(k + 1):
        first = first.next
        
    while first:
        first = first.next
        second = second.next
        
    second.next = second.next.next
    return dummy.next

# Khởi tạo: 1 -> 2 -> 3 -> 4 -> 5, k = 2
h3 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
h3 = remove_nth_from_end(h3, 2)
curr = h3
while curr:
    print(curr.val, end=" ")
    curr = curr.next
print()