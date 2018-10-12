""" Problem 4 - Dictionary Anagram Finder """

import itertools

class DictReader(object):
    """ Basic anagram finder with no caching """
    
    def __init__(self):
        self._anagrams = {}
        
    def index(self, dictfile):
        """ Index a dictionary file """

        print 'Start index.'
        for word in open(dictfile):
            word = word.strip()
            sig = hash(''.join(sorted(list(word.lower()))))
            # Calculate a "signature"

            try:
                self._anagrams[sig].append(word)
            except KeyError:
                self._anagrams[sig] = [word]

        print 'End index,found',len(self._anagrams),'anagrams.'

    def anagrams(self, word):
        """ Print anagrams for a given word """

        sig = hash(''.join(sorted(list(word.lower()))))
        result = self._anagrams.get(sig)

        return result
        
if __name__ == "__main__":
    import sys
    
    d = DictReader()
    d.index('/usr/share/dict/words')
    word = sys.argv[1]

    all_anagrams = []
    for i in range(2, len(word)):
        for item in itertools.permutations(word, i):
            subword = ''.join(item)

            try:
                all_anagrams += d.anagrams(subword)
            except:
                pass

    all_anagrams = sorted(list(set([x.lower() for x in all_anagrams])))
    open('anagrams.txt','w').writelines([s+'\n' for s in all_anagrams])
    
    # print sorted(d._anagrams.values(), key=len, reverse=True)[:3]
    # d.anagrams('crates')
    # d.anagrams('trap')
    # d.anagrams('hibernate')
