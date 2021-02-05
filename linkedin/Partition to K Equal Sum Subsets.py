class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        summ = sum(nums)
        if summ % k: return False
        nums.sort(reverse=True)
        target = summ // k
        res = []

        def dfs(idx, cur, group, l):
            nonlocal nums
            if group == k:
                return True
            if cur == target:
                res.append(l)
                return dfs(0, 0, group + 1, [])
            if cur > target: return False
            for i in range(idx, len(nums)):
                if nums[i] < 0: continue
                num = nums[i]
                nums[i] *= -1
                if dfs(i + 1, cur + num, group, l + [num]): return True
                nums[i] *= -1
            return False

        ans = dfs(0, 0, 0, [])
        print(res)
        return ans
