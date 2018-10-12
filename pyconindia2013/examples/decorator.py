""" Simple decorator for type checking """

def isNumber(f):
    def wrapper(*args):
        if not all(type(item) in (int, float) for item in args):
            raise TypeError,'Wrong type!'
        return f(*args)
    return wrapper

@isNumber
def add(x,y):
    return x+y
        
@isNumber
def mul(x,y):
    return x*y

if __name__ == "__main__":
    print add(3, 4)
    print mul(5,6)
    add(4, 'me')
