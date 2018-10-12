from matrix import MatrixFactory
import matrixops
import sys

def test(n=10):
    """ Demo multiplication of two square matrices of given dimension 'n' using concurrent multiplication """

    print('Making two random square matrices of dimension',n,'...')
    m1 = MatrixFactory.makeRandom(n, n)
    m2 = MatrixFactory.makeRandom(n, n)

    ops = matrixops.FastMatrixOps()
    m3 = ops.multiply(m1, m2)
    print(m3)

if __name__ == "__main__":
    try:
        test(n=int(sys.argv[1]))
    except:
        test()
