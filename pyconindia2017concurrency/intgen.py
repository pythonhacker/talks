import random

nums=list(range(10, 1000000))
    
for i in range(10000):
    mynums = random.sample(nums, 1000)
    # Write first 1000 numbers in a file
    fname = 'numbers/num_%d.txt' % (i + 1)
    print('Making',fname,'...')
    
    open(fname, 'w').writelines(map(lambda x: str(x) + '\n', mynums))
