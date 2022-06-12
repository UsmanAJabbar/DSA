from src import ListNode
def remove_nth_node_from_end(head: ListNode, n: int):
    """
    ------------------------
    Remove nth node from end
    ------------------------
    Description:
        Removes the nth-last node from the list
    """
    # The goal here is to a barrier such that
    # left ends up being the node before the node to be removed

    right = left = head

    for _ in range(n):
        right = right.next

    if not right:
        return head.next

    # Pull the barrier to the end while maintaining the gap
    # left.next should be the node to be deleted
    # Since this is Python, we could simply ignore freeing
    # memoring and setting left.next = left.next.next
    while right.next:
        left = left.next
        right = right.next

    left.next = left.next.next

    return head
