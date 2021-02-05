# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = [(head.val, i, head) for i, head in enumerate(lists) if head]
        dummy = ListNode()
        heapq.heapify(heap)
        p = dummy
        while heap:
            v, i, node = heapq.heappop(heap)
            p.next = node
            p = p.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next
