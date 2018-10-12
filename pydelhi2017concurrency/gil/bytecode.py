import sys
import time

i=100000
while i < sys.maxint - 1000:
    print '\tMax=>',max(xrange(i))
    i = i*10
    time.sleep(2)
