import requests
import time

urls=['http://www.google.com','http://www.cnn.com','http://www.arstechnica.com',
      'http://www.linkedin.com','http://wwww.gnu.org','http://www.linuxmint.com']

count=0

while count<20:
    for url in urls:
        print 'Fetched',requests.get(url)
    time.sleep(2)
    count += 1
