"""

Fast operations on a matrix class

"""

import multiprocessing
from matrix import Matrix, MatrixFactory
from functools import partial

# Debugging
logger = multiprocessing.log_to_stderr()
logger.setLevel(multiprocessing.SUBDEBUG)

def calc_row(r, m1, m2):
    """ Calculate a row 'r' of the multiplication output of matrices m1 and m2 """

    d = {}
    print('Calculating for',r)
    for y in range(m2.m):
        d[(r, y)] = sum(item[0]*item[1] for item in zip(m1.rows[r], m2[y]))

    return d

def calc_row2(r, m1, m2):
    """ Calculate a row 'r' of the multiplication output of matrices m1 and m2 """

    d = []
    print('Calculating for',r)
    for y in range(m2.m):
        # import pdb;pdb.set_trace()
        # import forkedpdb;forkedpdb.ForkedPdb().set_trace()      
        d.append(sum(item[0]*item[1] for item in zip(m1.rows[r], m2[y])))
        # d.append(sum(item[0]*item[1] for item in zip(m1.rows[r], m2[y])))
        # import forkedpdb;forkedpdb.ForkablePdb().set_trace()      

    return d

class FastMatrixOps(object):
    """ Fast operations on the matrix """

    @classmethod
    def multiply(self, m1, m2):
        """ Concurrently multiply two matrices using multiprocessing """

        matm, m2_n = m2.getRank()

        # Number of columns of m1 == Number of rows of m2
        if (m1.n != matm):
            raise MatrixError("Matrices cannot be multipled!")
        
        m2_t = m2.getTranspose()
        mulmat = Matrix(m1.m, m2_n)        

        # Matrix multiplication theorem
        # C = A x B then
        #
        #          k= m 
        # C(i,j) = Sigma A(i,k)*B(k,j)
        #          k = 1
        #
        # where m => number of rows of A

        # If  rank of A => (m, n)
        # and rank of B => (n, p)
        # Rank of C => (m, p)

        mul_partial = partial(calc_row, m1=m1, m2=m2_t)

        pool = multiprocessing.Pool(2)
        # Parallelize each row multiplication
        for row_dict in pool.map(mul_partial, range(m1.m)):
            for k,v in row_dict.items():
                x, y = k
                mulmat[x][y] = v
        # print output

        return mulmat

    @classmethod
    def multiply2(self, m1, m2):
        """ Concurrently multiply two matrices using multiprocessing - version 2 """


        matm, m2_n = m2.getRank()

        # Number of columns of m1 == Number of rows of m2
        if (m1.n != matm):
            raise MatrixError("Matrices cannot be multipled!")
        
        m2_t = m2.getTranspose()

        # Matrix multiplication theorem
        # C = A x B then
        #
        #          k= m 
        # C(i,j) = Sigma A(i,k)*B(k,j)
        #          k = 1
        #
        # where m => number of rows of A

        # If  rank of A => (m, n)
        # and rank of B => (n, p)
        # Rank of C => (m, p)

        mul_partial = partial(calc_row2, m1=m1, m2=m2_t)

        pool = multiprocessing.Pool(2)
        # Parallelize each row multiplication
        # data = pool.map(mul_partial, m1.m)      
        data = pool.map(mul_partial, range(m1.m))
        # print data

        # Build directly
        mulmat = MatrixFactory.fromList(data)
        
        return mulmat   

if __name__ == "__main__":
    # Make random matrix of rank (10, 10)
    m1 = MatrixFactory.makeRandom(10, 10)
    # Make second random matrix of rank (10, 10)    
    m2 = MatrixFactory.makeRandom(10, 10)   

    print('Calculating m1*m2 directly...')
    m3 = m1*m2
    
    fops = FastMatrixOps()
    print('Calculating m1*m2 concurrently using dictionaries...')
    m3_n = fops.multiply(m1, m2)
    print('Asserting both are equal...')
    print(m3 == m3_n)
    assert(m3 == m3_n)

    print('Calculating m1*m2 concurrently using direct data...')
    m3_n = fops.multiply2(m1, m2)
    print('Asserting both are equal...')
    print(m3 == m3_n)
    assert(m3 == m3_n)  
