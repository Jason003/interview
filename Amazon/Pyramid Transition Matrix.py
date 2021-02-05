'''
Input: bottom = "BCD", allowed = ["BCG", "CDE", "GEA", "FFF"]
Output: true
Explanation:
We can stack the pyramid like this:
    A
   / \
  G   E
 / \ / \
B   C   D

We are allowed to place G on top of B and C because BCG is an allowed triple.  Similarly, we can place E on top of C and D, then A on top of G and E.
'''

import collections
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        d = collections.defaultdict(set)
        for s in allowed:
            d[s[:2]].add(s[2])

        def helper(bottom, idx, nxt):
            if len(bottom) == 1: return True
            if idx == len(bottom) - 1: return helper(nxt, 0, '')
            s = bottom[idx: idx + 2]
            for c in d[s]:
                if helper(bottom, idx + 1, nxt + c): return True
            return False

        return helper(bottom, 0, '')
