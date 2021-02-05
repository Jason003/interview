def validMatrix(A):
    if not A: return True
    n = len(A)
    correctSet = set(range(1, n + 1))
    for i in range(n):
        rowSet = set()
        colSet = set()
        for j in range(n):
            rowSet.add(A[i][j])
            colSet.add(A[j][i])
        if rowSet != correctSet or colSet != correctSet:
            return False
    return True

A = [[1,2,3], [3,1,2],[1,3,2]]
print(validMatrix(A))

# nonogram

def isValidNonogram(matrix, rows, cols):
    if not matrix or not rows or not cols: return False
    m, n = len(matrix), len(matrix[0])
    if m != len(rows) or n != len(cols): return False

    def isValidNonogramRow(matrix, rows):
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            curr = []
            cnt = 0
            for j in range(n):
                if matrix[i][j] not in(1, 0): return False
                if matrix[i][j] == 0:
                    cnt += 1
                else:
                    if cnt:
                        curr.append(cnt)
                    cnt = 0
            if cnt:
                curr.append(cnt)
            if curr != rows[i]:
                return False
        return True
    return isValidNonogramRow(matrix, rows) and isValidNonogramRow(list(zip(*matrix)), cols)
matrix1 = [
    [1,1,1,1], # []
    [0,1,1,1], # [1] -> a single run of _1_ zero (i.e.: "0")
    [0,1,0,0], # [1, 2] -> first a run of _1_ zero, then a run of _2_ zeroes
    [1,1,0,1], # [1]
    [0,0,1,1], # [2]
]

# True
rows1_1 = [[],[1],[1,2],[1],[2]]
columns1_1 = [[2,1],[1],[2],[1]]
print(isValidNonogram(matrix1, rows1_1, columns1_1))
# False
rows1_2 = [[],[],[1],[1],[1,1]]
columns1_2 = [[2],[1],[2],[1]]
print(isValidNonogram(matrix1, rows1_2, columns1_2))
matrix2 = [
    [1,1],
    [0,0],
    [0,0],
    [1,0]
]
# False
rows2_1 = [[],[2],[2],[1]]
columns2_1 = [[1,1],[3]]
print(isValidNonogram(matrix2, rows2_1, columns2_1))