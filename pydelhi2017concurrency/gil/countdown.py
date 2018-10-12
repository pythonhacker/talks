import time
import threading

def countdown(n):
    while n>0:
        print "T-minus",n
        n -= 1
        time.sleep(1)

    print "Blastoff!"

    
threading.Thread(target=countdown, args=(100,)).start()
