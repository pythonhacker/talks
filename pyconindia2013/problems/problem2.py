""" Problem 2 - Find circular primes """

sieve = lambda n: not any(n % num==0 for num in range(2, int(pow(n,0.5))+1))

def rotations(num):
    """ Get all rotations of a number """

    # abc => bca, cab
    s = str(num)
    st = s*2
    return [int(st[i:i+len(s)]) for i in range(1,len(s))]
    
    
# Basic implementation
def circular_prime(limit):
    """ Find circular primes < limit """

    for i in range(2, limit):
        if sieve(i) and all(sieve(x) for x in rotations(i)):
            yield i
            
if __name__ == "__main__":
    for i in circular_prime(100):
        print i
