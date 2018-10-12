import os
import sys
import functools
import itertools

def checker(wordlist, filename):
    """ Return if the file matches all words in the word list """
    
    content = open(filename).read().lower().split()
    return all(word in content for word in wordlist)

def word_checker(folder, *words):
    """ Check a folder for a file containing the
    list of words. Stop after first hit """

    func = functools.partial(checker, words)

    for root, dirs, files in os.walk(folder):
        filenames = [os.path.join(root,f) for f in files]
        fileresults = list(itertools.dropwhile(lambda x: not func(x), filenames))
        if fileresults:
            return fileresults[0]
        

if __name__ == "__main__":
    print 'Filename is',word_checker('.',*sys.argv[1:])


