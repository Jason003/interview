class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


def getIntersectionNode(headA, headB):
    a, b = headA, headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a


def judgeIntersectionIfWithCicle(headA, headB):
    def detectCycle(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        f, s = head, head  # fast and slow
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f: break
        if not f or not f.next or not s: return None
        s = head
        while s != f:
            s = s.next
            f = f.next
        return s

    enterPointA, enterPointB = detectCycle(headA), detectCycle(headB)
    if not enterPointA and not enterPointB:  # if both of them don't have a circle
        return getIntersectionNode(headA, headB)

    if enterPointA and not enterPointB or enterPointB and not enterPointA:  # if one of them has a circle, they won't intersect
        return False

    # if both have circle

    # if they have same enter-circle point
    if enterPointA == enterPointB:
        enterPointA.next = None
        return getIntersectionNode(headA, headB)
    else:
        return enterPointA, enterPointB

        # p = enterPointA.next
        # while p != enterPointA:
        #     if p == enterPointB:
        #         return enterPointA, enterPointB
        #     p = p.next
        # return None


root1 = ListNode(1)
root2 = ListNode(2)



a = ListNode(3)
b = ListNode(4)
c = ListNode(5)
d = ListNode(6)
f = ListNode(7)
a.next = b
b.next = c
c.next = d

root1.next = f
root2.next = a
f.next = a
print(judgeIntersectionIfWithCicle(root1, root2))
