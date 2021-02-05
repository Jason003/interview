class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = [0] * len(T)
        for i, t in enumerate(T):
            while stack and t > T[stack[-1]]: # monotonous decreasing stack
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res