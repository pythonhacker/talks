# twisted_fetch_url.py
from twisted.internet import reactor
from twisted.web.client import getPage
import sys

def processPage(page, filename='content.html'):
    print type(page)
    open(filename,'w').write(page)
    print 'Data saved to',filename

def logError(error):
    print error

def finishProcessing(value):
    print "Shutting down..."
    reactor.stop()

if __name__ == "__main__":
    url = sys.argv[1]
    deferred = getPage(url) 
    deferred.addCallbacks(processPage, logError)
    deferred.addBoth(finishProcessing)

    reactor.run()
