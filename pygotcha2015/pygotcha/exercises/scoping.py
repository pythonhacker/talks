"""

Fix the error in the global variable scoping and
in using the locals() dictionary in local variable
modification.

"""

X,Y=100,200

def add_if(x, y):
    """ Add two numbers to global X & Y
    and return the value """
    
    if x<500:
        X += x
        
    if y<400:
        Y += y

    z = X + Y
    return z

def foo(x, y):
    """ A simple function """

    z = x + y
    if z>100:
        # Modify X
        locals()['X'] = z + X
    elif z>50:
        # Modify X
        locals()['X'] = z + Y       

    print 'X=>',X
    return z

if __name__ == "__main__":
    print add_if(400, 500)
    #foo(30, 40)
    #foo(60, 70)
