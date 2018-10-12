""" Caching decorator example """

def cache(f):
    results = {}
    def wrapper(*args):
        if args in results:
            print 'From cache'
            return results[args]
        res = f(*args)
        results[args] = res
        return res

    return wrapper

@cache
def factorial(n):
    """ Factorial of a number """
    
    return reduce(lambda x,y: x*y, range(1,n+1))

if __name__ == "__main__":
    print factorial(5)
    print factorial(10) 
    print factorial(5)  
