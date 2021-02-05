class Solution:
    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
        res = []

        def dfs(cur, candidates):
            if len(cur) == len(nums):
                res.append(list(cur))
                return
            for num in candidates:
                dfs(cur + [num], candidates - {num})

        dfs([], set(nums))
        return res
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def helper(curr):
            if len(curr) == len(nums):
                res.append(curr)
                return
            for i, num in enumerate(nums):
                if i > 0 and nums[i] == nums[i - 1]: continue
                if num != '#':
                    nums[i] = '#'
                    helper(curr + [num])
                    nums[i] = num
        helper([])
        return res