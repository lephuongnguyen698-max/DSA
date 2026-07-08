def addTwoNumbers(l1, l2):
    dummy = Node(0)
    curr = dummy
    carry = 0

    while l1 or l2 or carry:
        total = carry

        if l1:
            total += l1.data
            l1 = l1.next

        if l2:
            total += l2.data
            l2 = l2.next

        carry = total // 10

        curr.next = Node(total % 10)
        curr = curr.next

    return dummy.next