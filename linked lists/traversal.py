def get_sum(head):
    ans = 0
    while head:
        ans += head.val
        head = head.next

    return ans


# Recursion

def getSum(head):
    if not head:
        return None
    return head.val + getSum(head.next)
