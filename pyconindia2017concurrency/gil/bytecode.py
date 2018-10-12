import sys
import time

i=100000
while i < sys.maxsize - 1000:
    print('\tMax=>',max(range(i)))
    i = i*10
    time.sleep(2)
