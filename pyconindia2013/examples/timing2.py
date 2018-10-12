""" Timing tests#2 for punctuation replace functions """

from itertools import imap, chain, ifilter
from functimer import functimer

import string
import re

punc = string.punctuation

def repl_listcomp(strings):
    return [[i for i in s if i not in punc] for s in strings]

def repl_functional(strings):
    return map(lambda x: [i for i in x if i not in punc],strings)    

def repl_itertools1(strings):
    return list(imap(lambda x: [i for i in x if i not in punc],strings))

def repl_itertools2(strings):
    return list(ifilter(lambda x: x not in punc, chain(*strings)))
def repl_listcomp(strings):
    return [[i for i in s if i not in punc] for s in strings]

def repl_functional(strings):
    return map(lambda x: [i for i in x if i not in punc],strings)    

def repl_itertools1(strings):
    return list(imap(lambda x: [i for i in x if i not in punc],strings))

def repl_itertools2(strings):
    return list(ifilter(lambda x: x not in punc, chain(*strings)))

def repl_re(strings):
    return [re.sub('[' + punc + ']+', '', x) for x in strings]

if __name__ == "__main__":
    strings = ['#I love,@,#',' PyCon India..$#,']
    print 'Listcomp =>',functimer(repl_listcomp, strings)
    print 'Functional =>',functimer(repl_functional, strings) 
    print 'Itertools #1 =>',functimer(repl_itertools1, strings)
    print 'Itertools #2 =>',functimer(repl_itertools2, strings) 
