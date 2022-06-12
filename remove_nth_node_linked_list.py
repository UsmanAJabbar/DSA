def remove_nth_node_from_end(head, n)
    right = left = head

    for i in range(n):
        right = right.next

    if not right:
        return head.next

    while right.next:
        left = left.next
        right = right.next
        
    left.next = left.next.next

    return head
