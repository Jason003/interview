class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        curr = head
        while curr and curr.next:
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = dummy.next
            dummy.next = nxt
        return dummy.next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        res = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return res