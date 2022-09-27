class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next():
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


# Given the head of a linked list and an integer k, return the k^{th}k
def find_node(head, k):
    slow = head
    fast = head
    for _ in range(k):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    return slow
