""" Itertools examples """

import itertools
import collections
import operator
import os

# itertools.count can provide an infinite counter.
for i in itertools.count(step=1):
    print i
    if i == 20: break
    
# itertools.cycle cycles through an iterator
# Will keep printing 'python'

for i,j in enumerate(itertools.cycle(['python'])):
    print j
    if i==10: break

# itertools.repeat keeps repeating from an iterator
# Will keep producing range(10) when called in a loop
print itertools.repeat(range(10))

# chain returns elements from 'n' iterators until they are exhausted.

# Make a dictionary of count of letters in a list of strings.
birds = ['parrot','crow','dove','peacock','macaw','hen']
frequency = collections.defaultdict(int)
for letter in itertools.chain(*birds):
    frequency[letter] += 1                  

print frequency            
# takewhile returns elements as long as a predicate(condition) is True.

# Give list of favorable countries
countries=['U.S','U.K','India','Australia','Malaysia','Pakistan']           
print list(itertools.takewhile(lambda x: x != 'Pakistan', countries))


# dropwhile keeps dropping elements while predicate is True.

# Produce iterator of files > a minimum size in current folder.
files = sorted([(file, os.path.getsize(file)) for file in os.listdir(".")],
               key=operator.itemgetter(1))
print list(itertools.dropwhile(lambda x: x[1] < 8192, files))        
