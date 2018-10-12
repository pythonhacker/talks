"""
Fix the code to perform float division and fix the assertion

"""

import fractions

def check(x, y):
    """ A function checking for fractions """
    
    ans = 1.0*x/y
    # check fractional part
    assert(fractions.Fraction(ans).denominator > 1)

if __name__ == "__main__":
    check(5,2)
