""" Indenting context manager """

from contextlib import contextmanager

spaces = 0

@contextmanager
def indent():
    global spaces
    spaces += 1
    print '\t'*spaces,
    yield
    spaces -= 1

class Indent(object):

    def __init__(self):
        self.spaces = 0
        
    def __enter__(self):
        self.spaces += 1
        print '\t'*self.spaces,

    def __exit__(self, type, value, traceback):
        self.spaces -= 1

if __name__ == "__main__":
    for i in range(2,5):
        with indent():
            print 'This is number',i
            with indent():
                print 'This is its square',i*i

    for i in range(2,5):
        indenter = Indent()
        with indenter:
            print 'This is number',i
            with indenter:
                print 'This is its square',i*i              
                
            
    
