""" Problem 4 - Dictionary Anagram Finder """

import collections
import cPickle
import os

class DictReader(object):
    """ Anagram finder with caching """
    
    def __init__(self):
        self._anagrams = collections.defaultdict(list)
        self.indexfile = '.index'
        self.cachefile = '.cache'
        self._cache = {}
        # Load cache
        self._load_cache()
        self._dump = cPickle.dump
        
    def _load_cache(self):

        if os.path.isfile(self.cachefile):
            print 'Loaded cache.'
            self._cache = cPickle.load(open(self.cachefile,'rb'))
            
    def cache(f):
        def wrapper(self, *args):
            if args in self._cache:
                print 'From cache'
                return self._cache[args]
            res = f(self, *args)
            self._cache[args] = res
            return res

        return wrapper

    def __del__(self):
        # Write cache to disk before getting deleted
        if self._cache:
            self._dump(self._cache, open(self.cachefile,'wb'))
        
    def get_signature(self, word):
        """ Return signature of the word """

        return hash(''.join(sorted(list(word.lower()))))
            
    def index(self, dictfile='/usr/share/dict/words'):
        """ Index a dictionary file """
        
        if os.path.isfile(self.indexfile):
            self._anagrams = cPickle.load(open(self.indexfile,'rb'))
            print 'Loaded index.'
        else:
            print 'Start index.'
        
            for word in open(dictfile):
                word = word.strip()
                sig = self.get_signature(word)
                # Calculate a "signature"
                self._anagrams[sig].append(word)

            print 'End index,found',len(self._anagrams),'anagrams.'
            # Save index
            self._dump(self._anagrams, open(self.indexfile,'wb'))
            print 'Saved index.'

    @cache
    def anagrams(self, word):
        """ Print anagrams for a given word """

        result = self._anagrams.get(self.get_signature(word))
        return result
        
        
if __name__ == "__main__":
    d = DictReader()
    d.index('/usr/share/dict/words')
    # print sorted(d._anagrams.values(), key=len, reverse=True)[:3]
    print d.anagrams('crates')
    print d.anagrams('crates')  
    print d.anagrams('traps')
