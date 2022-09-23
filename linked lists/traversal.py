def get_sum(head):
    ans = 0
    while head:
        ans += head.val
        head = head.next

    return ans

