'''
instead of calculating area by height*width, we can think it in a cumulative way. In other words, sum water amount of each bin(width=1).
Search from left to right and maintain a max height of left and right separately, which is like a one-side wall of partial container. Fix the higher one and flow water from the lower part. For example, if current height of left is lower, we fill water in the left bin. Until left meets right, we filled the whole container.
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxLeft, maxRight = 0, 0
        res = 0
        while l < r:
            if height[l] < height[r]:
                maxLeft = max(maxLeft, height[l])
                res += maxLeft - height[l]
                l += 1
            else:
                maxRight = max(maxRight, height[r])
                res += maxRight - height[r]
                r -= 1
        return res