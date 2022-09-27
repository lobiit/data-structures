def get_head(head):
    length = 0
    dummy = head
    while dummy:
        length += 1
        dummy = dummy.next
    for i in range(length//2):
        head = head.next
    return head.val
