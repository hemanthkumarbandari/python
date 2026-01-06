class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        behind = dummy
        ahead = dummy

        for _ in range(n + 1):
            ahead = ahead.next

        while ahead:
            ahead = ahead.next
            behind = behind.next

        behind.next = behind.next.next
        return dummy.next
