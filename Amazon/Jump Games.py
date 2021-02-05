'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        mx = 0
        while i < len(nums) and i <= mx:
            mx = max(mx, i + nums[i])
            i += 1
        return i == len(nums)

'''
Follow up: 
What is the minimum steps to reach the last index?
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        mx = 0
        steps = 0
        while mx < len(nums) - 1:
            temp = mx
            while i < len(nums) and i <= temp:
                mx = max(mx, i + nums[i])
                i += 1
            steps += 1
            if mx == temp: return -1
        return steps


'''
Jump Game III:
Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.
'''
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        dq = collections.deque([start])
        seen = {start}
        while dq:
            curr = dq.popleft()
            if arr[curr] == 0:
                return True
            for nxt in (curr + arr[curr], curr - arr[curr]):
                if 0 <= nxt < len(arr) and nxt not in seen:
                    seen.add(nxt)
                    dq.append(nxt)
        return False