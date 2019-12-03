def triplet(A):
    if len(A) < 3:
        return False
    A.sort()
    for i in range(len(A) - 2):
        if A[i] > 0 and A[i] + A[i + 1] > A[i + 2]:
            return True
    return False
