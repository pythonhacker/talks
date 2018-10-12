""" Matrix class as an example for zip to transpose lists """

import random

class MatrixA:       
    def __init__(self,m,n):
        self.m, self.n = m,n
        self.rows=[[random.randrange(1,10) for j in range(n)] for i in range(m)]

    def __str__(self):
        s='\n'.join([' '.join([str(item) for item in row]) for row in self.rows])
        return s + '\n'

    def transpose(self):

        rows2 = [[0]*self.m for i in range(self.n)]
        for x in range(self.m):
            for y in range(self.n):
                rows2[y][x] = self.rows[x][y]

        self.rows = rows2
        # Swap m and n
        tmp = self.m
        self.m = self.n
        self.n = tmp

class MatrixB(MatrixA):

    def transpose(self):
        self.m, self.n = self.n, self.m
        self.rows = zip(*self.rows)

if __name__ == "__main__":
    m = MatrixA(3,4)
    print m
    m.transpose()
    print m

    m = MatrixB(3,4)
    print m
    m.transpose()
    print m
