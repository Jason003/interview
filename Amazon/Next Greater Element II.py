class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = []
        for i, num in enumerate(nums + nums):
            while stack and nums[stack[-1]] < num:
                res[stack.pop()] = num
            if i < len(nums): stack.append(i)
        return res