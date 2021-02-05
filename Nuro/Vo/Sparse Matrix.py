class Sparse_Matrix:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.data = [[0] * 3 for _ in range(10000)]
        self.len = 0

    def insert(self, m, n, v):
        self.data[self.len][0] = m
        self.data[self.len][1] = n
        self.data[self.len][2] = v
        self.len += 1

    '''
    Addition operation traverses the matrices linearly, hence, has a time complexity of O(n), where n is the number of non-zero elements in the larger matrix amongst the two.
    '''
    def add(self, b):
        if self.m != b.m or self.n != b.n:
            raise Exception('Matrix can not be added')
        i, j = 0, 0
        res = Sparse_Matrix(self.m, self.n)
        while i < self.len or j < b.len:
            if i == self.len:
                res.insert(*b.data[j])
                j += 1
            elif j == b.len:
                res.insert(*self.data[i])
                i += 1
            elif self.data[i][0] < b.data[j][0] or self.data[i][0] == b.data[j][0] and self.data[i][1] < b.data[j][1]:
                res.insert(*self.data[i])
                i += 1
            elif self.data[i][0] > b.data[j][0] or self.data[i][0] == b.data[j][0] and self.data[i][1] > b.data[j][1]:
                res.insert(*b.data[j])
                j += 1
            else:
                res.insert(self.data[i][0], self.data[i][1], self.data[i][2] + b.data[j][2])
                i += 1
                j += 1
        return res

    def transpose(self): # Transpose has a time complexity of O(n+m), where n is the number of columns and m is the number of non-zero elements in the matrix.
        res = Sparse_Matrix(self.n, self.m)
        res.len = self.len
        cnt = [0] * (self.n + 1) # count the number of elements in each column
        for i, j, v in self.data[:self.len]:
            cnt[j] += 1
        index = [0] * (self.n + 1) # get the starting index for each column
        for i in range(1, self.n + 1):
            index[i] = index[i - 1] + cnt[i - 1]
        for i, j, v in self.data[:self.len]:
            res.data[index[j]][0] = j
            res.data[index[j]][1] = i
            res.data[index[j]][2] = v
            index[j] += 1
        return res

    def multiply(self, b):
        # Multiplication, however, has a time complexity of O(x*n + y*m), where (x, m) is number of columns and terms in the second matrix; and (y, n) is number of rows and terms in the first matrix.
        if self.n != b.m:
            raise Exception('Invalid dimension')
        b = b.transpose()
        i = 0
        res = Sparse_Matrix(self.m, b.m)
        while i < self.len:
            r = self.data[i][0]
            j = 0
            while j < b.len:
                c = b.data[j][0] # b is transposed
                tempi, tempj = i, j
                summ = 0
                while tempi < self.len and self.data[tempi][0] == r and tempj < b.len and b.data[tempj][0] == c:
                    if self.data[tempi][1] < b.data[tempj][1]:
                        tempi += 1
                    elif self.data[tempi][1] > b.data[tempj][1]:
                        tempj += 1
                    else:
                        summ += self.data[tempi][2] * b.data[tempj][2]
                        tempi += 1
                        tempj += 1
                if summ:
                    res.insert(r, c, summ)
                while j < b.len and b.data[j][0] == c:
                    j += 1
            while i < self.len and self.data[i][0] == r:
                i += 1
        return res


m1 = Sparse_Matrix(2, 2)
m2 = Sparse_Matrix(2, 2)
m1.insert(0,0,1)
m1.insert(0,1,1)
m1.insert(1,1,1)
m2.insert(0,0,1)
m2.insert(1,1,1)

print(m1.multiply(m2).data)

a = Sparse_Matrix(4, 4)
b = Sparse_Matrix(4, 4)

a.insert(1, 2, 10)
a.insert(1, 4, 12)
a.insert(3, 3, 5)
a.insert(4, 1, 15)
a.insert(4, 2, 12)
b.insert(1, 3, 8)
b.insert(2, 4, 23)
b.insert(3, 3, 9)
b.insert(4, 1, 20)
b.insert(4, 2, 25)

print(a.multiply(b).data)
print(a.transpose().data)