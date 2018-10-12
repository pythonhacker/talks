"""

Miscellaneous gotchas - fix 'em.

"""

modul='Miscellaneous'

def mul_num(num, factor=5):
    """ Multiply number by factor """

    print type(num)
    print 'Number is ',num
    x = num*factor
    assert(type(x) == int)

def lucky_num(secret=7):
    """ Return your lucky number !"""

    x = int(raw_input("Give me your input number: "))
    print 'Your yucky number of the day is =>', x*10 % secret


if __name__ == "__main__":
    # try:
    # lucky_num()
        
    num = 20 
    mul_num(num)
    #    
    #except TypeError, AssertionError:
    #    print 'Hmmm this module',module,'has lot of issues right !'
    #    raise
    
