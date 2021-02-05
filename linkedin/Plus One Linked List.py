# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def plusOne(self, head):
        start = None

        node = head
        while node:
            if node.val < 9:
                start = node
            node = node.next

        if start:
            start.val += 1
            node = start.next
        else: # 99999
            new = ListNode(1)
            new.next = head
            node = head
            head = new

        while node:
            node.val = 0
            node = node.next

        return head
