"""

Fix the code to avoid the TypeError raised when the mutable is modified.

"""

import doctest


def create_webpage(page, html, index=0):
    """ Create a web page by inserting html snippet 'html' at index 'index'

    """

    page[index] += html

if __name__ == "__main__":
    page = (['head','title','script','script','body','div','div','p','p','div'],)
    create_webpage(page, ['p'], index=0)
    
