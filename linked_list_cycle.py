def linked_list_cycle(head) -> bool:
    turtle = hare = head

    while hare and hare.next:
        turtle = turtle.next
        hare = hare.next.next

        if turtle == hare:
            return True

    return False
