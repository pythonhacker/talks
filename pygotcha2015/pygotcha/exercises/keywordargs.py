"""

Fix the exception in the functions below that uses keyword arguments.

"""

def myfavlang(msg, extra, **kwargs):
    """ Print something nice about my favorite programming language """

    output = ' '.join((msg, kwargs.get('lang', 'Python'), '-',extra))
    print output


if __name__ == "__main__":
    myfavlang('I love','It is awesome!', lang='Python')
    # Fix this
    myfavlang('I love','It is awesome!', msg='Python', extra='Best for newbies.')  
