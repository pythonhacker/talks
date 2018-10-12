""" Simple web crawler using concurrent futures """

from concurrent.futures import ProcessPoolExecutor
from queue import Queue
import requests
import sys
import urllib
from bs4 import BeautifulSoup as bs

def fetch_url(url):
    response = requests.get(url)
    return (response.url, response.status_code, response.content)
    

if __name__ == "__main__":
    base_url = sys.argv[1]
    
    with ProcessPoolExecutor(max_workers=5) as executor:
        urls = [base_url]
        url_dict = {}
        url_dict[base_url] = 1
        
        while len(urls):
            results = executor.map(fetch_url, urls, timeout=120)
            urls = []
            
            for result in results:
                url, status, data = result
                if status == 200:
                    # Save and parse the text
                    print('Fetched',url)
                    soup = bs(data, "lxml")
                    # Fetch all child links
                    child_links = filter(None, [item.get('href', '') for item in soup.findAll('a')])
                    # Make full links
                    child_urls = [urllib.parse.urljoin(base_url, curl) for curl in child_links if curl[0] != '#']
                    # Push this to queue
                    for url in child_urls:
                        print('Pushing',url)
                        if not url in url_dict:
                            url_dict[url] = 1
                            urls.append(url)
                    
                
