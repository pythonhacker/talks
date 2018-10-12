""" Checking for sentinel values """

from itertools import takewhile,imap,cycle
import functools
import random

def solution_a(sentinel):

    # Solution A
    # Append numbers till you hit sentinel
    nums = []        

    while True:
        num = random.randrange(1, 100)
        if num == sentinel: break
        nums.append(num)

    return nums

def solution_b1(sentinel):

    func = functools.partial(random.randrange, 1, 100) 
    nums = []

    for num in iter(func, sentinel):    
        nums.append(num)    

    return nums

def solution_b2(sentinel):
    return list(takewhile(lambda x: x!=sentinel, 
                          imap(random.randrange, cycle([1]), cycle([100]))))


if __name__ == "__main__":
    print solution_a(41)
    print solution_b1(41)
    print solution_b2(41)   
