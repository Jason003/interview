class Solution:
    def canPlaceFlowers(self, A: List[int], n: int) -> bool:
        canPlace = 0
        for i in range(len(A)):
            if (i == 0 or A[i - 1] == 0) and (i == len(A) - 1 or A[i + 1] == 0) and A[i] == 0:
                A[i] = 1
                canPlace += 1
            if canPlace >= n: return True
        return False