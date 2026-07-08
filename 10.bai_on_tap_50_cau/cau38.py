def detect_cycle_start(head):
    slow = head
    fast = head
    has_cycle = False
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break
            
    if not has_cycle:
        return None
        
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
        
    return slow

# Khởi tạo đồ thị có chu trình
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
node3.next = node2 # Chu trình quay lại node 2

start_node = detect_cycle_start(node1)
print(start_node.val if start_node else "No cycle")