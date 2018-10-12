import os
import hashlib
import sys
import multiprocessing
import argparse
import time
import random

# ddbd8937e3ea972c806893273f4c667f -> ~/programs
# 056d25d9374bdbe20fff4acb7517c438 -> ~/Documents/../
# 1df687972c898a80118f332bcce637cd -> ~/Documents/../../../../
 
def check_hash(fpath, inhash):
    """ Verify hash """

    try:
        data = open(fpath, 'rb').read()
        
        fhash = hashlib.md5(data).hexdigest()
        if fhash == inhash:
            print('Found =>',fpath)
            return fpath

    except Exception as e:
        # print('Error processing filepath=>',fpath,'=>',e)
        pass
    
def detect(folder, inhash):
    """ Find a file which has a given MD5 hash and return it starting from a folder """
    
    for root,dirs,files in os.walk(folder):
        for f in files:
            fpath = root + '/' + f
            ret = check_hash(fpath, inhash)
            if ret == fpath:
                return fpath

def walk_path(path, file_q):

    files = []
    folders = []
    
    for filename in os.listdir(path):
        fullname = os.path.join(path, filename)
        # print('Fullname=>',fullname)
        
        if os.path.isdir(fullname):
            folders.append(fullname)
        else:
            file_q.put(fullname)

    # Shuffle a bit
    random.shuffle(folders)
    
    return folders
            
def parallel_walk(path_q, state, file_q):
    """ Parallel walk a folder to generate file paths inside it """

    while True:
        path = path_q.get()

        if state.value:
            print('End condition, Quitting')
            break
        
        # print('Got path=>',path)
        dirs = walk_path(path, file_q)
        for newdir in dirs:
            path_q.put(newdir)

def parallel_check_hash(file_q, state, inhash):
    """ Check hash of file in parallel """

    while True:
        filepath = file_q.get()

        if state.value:
            print('End condition, Quitting')
            break

        # print('Checking',filepath,'...')
        ret = check_hash(filepath, inhash)
        if ret == filepath:
            print('Found solution')
            state.value =  1
            break
        
        
def detect_concurrent(folder, inhash, concurrency=2):
    """ Find a file which has a given MD5 hash and return it - concurrent version """

    path_q = multiprocessing.Queue()
    path_q.put(folder)
    file_q = multiprocessing.Queue()    
    procs1 = []
    procs2 = [] 

    print('Using a concurency of',concurrency)
    cpu = concurrency # multiprocessing.cpu_count()
    # for IPC
    state = multiprocessing.Value('i', 0)
    
    for i in range(cpu):
        p = multiprocessing.Process(target=parallel_walk, args=(path_q, state, file_q))
        p.daemon = True
        procs1.append(p)
        p.start()

    for i in range(cpu):
        p = multiprocessing.Process(target=parallel_check_hash, args=(file_q, state, inhash))
        procs2.append(p)
        print('Starting',p)
        p.start()       

    for p in procs2:
        print('Joining2',p)      
        p.join()
        print('Joined2',p)

    #for p in procs1:
    #    print('Joining1',p)
    #    p.join()
    #    print('Joined1',p)      



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find a file, given a hash')
    parser.add_argument('-c','--concurrent',help='Concurrently solve using multiple processes', action='store_true')
    parser.add_argument('-p','--procs',help='Number of concurrent processes', default=2, type=int)
    parser.add_argument('-f','--folder',help='Folder to search for')
    parser.add_argument('hash',help='Hash string to look for')  
    
    args = parser.parse_args()

    if args.concurrent:
        detect_concurrent(args.folder, args.hash, args.procs)
    else:
        detect(args.folder, args.hash)      
