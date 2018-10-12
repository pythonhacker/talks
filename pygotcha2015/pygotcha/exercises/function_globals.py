"""

Fix the exceptions with trying to use output of reversed, enumerate etc as lists.

"""

def reverse_sort(inlist, index=0):
    """ Sort and reverse the input list and return
    item at index 'index' """

    rs_inlist = reversed(sorted(inlist))
    return rs_inlist[index]

def enumerate_sort(inlist, index=0):
    """ Sort and enumerate the input list and return
    item at index 'index' """

    es_inlist = enumerate(sorted(inlist))
    return es_inlist[index]

def reverse_enumerate_sort(inlist, index=0):
    """ Sort and reverse the input list and return
    item at index 'index' """

    res_inlist = reversed(enumerate(sorted(inlist)))
    return res_inlist[index]

def sort_reverse_enumerate(inlist, index=0):
    """ Sort, reverse and enumerate the input list
    and return item at index 'index' """

    sre_inlist = sorted(reversed(enumerate(inlist)))
    return sre_inlist[index]


if __name__ == "__main__":
    # Create list
    import random

    inlist = random.sample(range(10, 50), 10)

    #reverse_sort(inlist)
    #enumerate_sort(inlist)
    #reverse_enumerate_sort(inlist)
    print sort_reverse_enumerate(inlist)
    
