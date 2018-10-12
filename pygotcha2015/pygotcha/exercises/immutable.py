"""
Fix code for immutable variable comparison.
Make sure all doctests pass after your fix.

"""

import doctest

def get_error(msg, prefix, default_value='Error:'):
    """ Generate an error message given the
    actual message (msg) and a prefix (prefix)

    >>> get_error('Coredumped','Error:')
    'Error: Coredumped'
    
    """
    
    if prefix is not default_value:
        prefix = default_value + prefix

    error_msg = prefix + ' ' + msg
    return error_msg

# The following version is for the more experienced ones.

def get_errors(*args, **kwargs):
    """ Generate an error message given the
    actual message (msg) and a prefix (prefix)

    >>> get_errors('Coredumped', prefix='Error:')
    'Error: Coredumped'
    >>> get_errors('Coredumped', prefix='(system)')
    'Error: (system) Coredumped'
    
    """

    prefix = kwargs.get('prefix', 'Error:')
    if prefix is not 'Error:':
        prefix = 'Error: '+ prefix

    msg = ' '.join(args)
    
    error_msg = prefix + ' ' + msg
    return error_msg


    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    
