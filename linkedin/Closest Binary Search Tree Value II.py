'''
Time Complexity: O(k + logn)
Time complexity of getPredecessor and getSuccessor is amortized O(1) because it's just part of the inorder traversal.
'''
class Solution(object):
    def closestValue(self, root, target: float) -> int:
        if not root:
            raise Exception('Invalid Input!')
        diff = float('inf')
        res = None
        while root:
            if abs(root.val - target) < diff:
                diff = abs(root.val - target)
                res = root.val
            if root.val > target:
                root = root.left
            else:
                root = root.right
        return res

    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        ans = []
        preStack = [] # stores all the values less than target, increasing
        sucStack = [] # stores all the values greater than target, decreasing

        while root:
            if root.val < target:
                preStack.append(root)
                root = root.right
            else:
                sucStack.append(root)
                root = root.left

        def getPredecessor(stack):
            if stack:
                pre = stack.pop()
                p = pre.left # ensure that all the new values are less than target
                while p:
                    stack.append(p)
                    p = p.right
                return pre
            return None

        def getSuccessor(stack):
            if stack:
                suc = stack.pop()
                p = suc.right
                while p:
                    stack.append(p)
                    p = p.left
                return suc
            return None

        pre = getPredecessor(preStack)
        suc = getSuccessor(sucStack)

        while k:
            k -= 1
            if pre and not suc:
                ans.append(pre.val)
                pre = getPredecessor(preStack)
            elif not pre and suc:
                ans.append(suc.val)
                suc = getSuccessor(sucStack)
            elif pre and suc and abs(pre.val - target) <= abs(suc.val - target):
                ans.append(pre.val)
                pre = getPredecessor(preStack)
            elif pre and suc and abs(pre.val - target) >= abs(suc.val - target):
                ans.append(suc.val)
                suc = getSuccessor(sucStack)
        return ans

    def findClosestElements(self, arr, k: int, x: int):
        # O(nlogn)
        # return sorted(sorted(arr, key = lambda i: (abs(i - x), i))[:k])

        # O(log(n - k) + k)
        lo, hi = 0, len(arr) - k
        while lo < hi:
            mi = (hi - lo) // 2 + lo
            if x - arr[mi] > arr[mi + k] - x:
                lo = mi + 1
            else:
                hi = mi
        return arr[lo: lo + k]