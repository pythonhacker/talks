import os
import sys

def check(filename, *words):
    """ Find if the words are present in the file """

    content = open(filename).read().lower().split()
    return all(word in content for word in words)
    
def word_checker(folder, *words):
    """ Check a folder for a file containing the
    list of words. Stop after first word """

    found = False
    # Do this recursively
    for root, dirs, files in os.walk(folder):
        if found: break
        
        for fname in files:
            fullpath = os.path.join(root, fname)
            if check(fullpath, *words):
                print 'Found words at',fullpath
                found = True
                break

if __name__ == "__main__":
    word_checker('.',*sys.argv[1:])
