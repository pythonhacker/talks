"""

Fix the code to get the correct round-off for the floating point
number and fix the assertion

"""
import math

def roundup(frac, place=2):
    """ Round up a fraction to 'place' decimal places and check it has changed """

    frac_ = math.ceil(frac*100)/100
    # frac_ = round(frac, place)
    print frac_, frac
    # Will get an error below - how to fix it?
    assert(frac_ > frac)

if __name__ == "__main__":
    roundup(0.485)

 
