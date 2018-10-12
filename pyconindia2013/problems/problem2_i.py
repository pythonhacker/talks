""" Problem 2 - Find circular primes """
import itertools

def rotate(instring):
    """ Rotations generator """

    for i in range(1, len(instring)):
        yield instring[i:] + instring[:i]
    
def circular_prime_generator(limit):
    """ Generator for circular primes """

    sieve = lambda n: not any(n % num==0 for num in range(2, int(pow(n,0.5))+1))
    cond = lambda x: sieve(x) and all(sieve(int(y)) for y in rotate(str(x)))
    for i in itertools.ifilter(cond, itertools.count(start=2)):
        if i>limit: break
        yield i

if __name__ == "__main__":
    for i in circular_prime_generator(1000):
        print i


    
