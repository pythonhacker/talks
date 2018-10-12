"""

Fix the syntax for positional & keyword arguments.

"""

def foo(*args, lang='Python'):
    """ Print something nice about my favorite programming language """

    msg = ' '.join(args)
    output = ' '.join((msg, kwargs.get('lang', 'Python')))
    print output


if __name__ == "__main__":
    foo('I love','It is awesome!', lang='Python')

