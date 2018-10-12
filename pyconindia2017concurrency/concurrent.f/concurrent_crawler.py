""" Simple web crawler using concurrent futures """

from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import requests
import sys
import urllib
import re
import pickle
import zlib
import argparse

from bs4 import BeautifulSoup as bs

www_re = re.compile(r'^www\d*\.', re.IGNORECASE)
skip_re = re.compile(r'(javascript:)|(javascript\([^\)]*\))|(mailto:)|(news:)|(webcal:)|(tel:)')
    
def get_domain(url):
    """ Given URL, return domain """

    if not (url.startswith('http://') or url.startswith('https://')):
        url = 'http://' + url
        
    return www_re.sub('', urllib.parse.urlparse(url).netloc).strip()

class Crawler(object):
    """ A dead simple recursive single-domain web-crawler using concurrent futures """

    def __init__(self, url, directory=False, concurrency=5, threads=False):
        # Crawl as a directory (dont crawl entire domain)
        self.directory = directory
        # Concurrency in terms of number of workers
        self.concurrency = concurrency
        # This crawler only crawls the same domain
        self.url = url
        # Calculate domain
        self.domain = get_domain(self.url)
        # Calculate path
        self.urlp = urllib.parse.urlparse(self.url)
        # Count of fetched URLs
        self.count = 0
        # Map of saved data
        self.data_map = {}
        # Use threads ?
        self.threads = threads

    def fetch_url(self, url):

        if not url.startswith('http'):
            url = 'http://' + url
            
        try:
            response = requests.get(url, timeout=30)
            return (response.url, response.status_code, response.content)
        except Exception as e:
            print('Error fetching URL =>', e)


    def parse_child_links(self, url, data):
        """ Parse and return child links """
        
        soup = bs(data, "lxml")
        # Fetch all child links
        child_links = filter(None, [item.get('href', '') for item in soup.findAll('a')])
        child_urls = []
        
        # Make full links
        for curl in child_links:
            # print(curl)
            if (curl[0] == '#') or skip_re.search(curl):
                # print('Skipping',curl)
                continue
            
            child_url = urllib.parse.urljoin(url, curl)
            # print(child_url)
            # Check domain
            domain = get_domain(child_url)
            if domain != self.domain:
                continue

            # If directory crawl, the child URL path has to match base URL path
            if self.directory:
                cpath = urllib.parse.urlparse(child_url)
                # If this is a sub-path of the base-path - then cool
                if not cpath.path.startswith(self.urlp.path):
                    continue
            
            child_urls.append(child_url)

        return child_urls
        
    def crawl(self):
        """ Crawl a site recursively """

        if self.threads:
            executor = ThreadPoolExecutor(max_workers = self.concurrency)
        else:
            executor = ProcessPoolExecutor(max_workers = self.concurrency)

        with executor:
            urls = [self.url]
            url_dict = {}
            url_dict[self.url] = 1

            while len(urls):
                results = executor.map(self.fetch_url, urls, timeout=120)
                urls = []x`

                for result in results:
                    url, status, data = result
                    if status in (200, 301, 302):
                        # Save and parse the text
                        print('Fetched',url)
                        self.count += 1
                        self.data_map[url] = data
                        child_urls = self.parse_child_links(url, data)
                        
                        # Push this to queue
                        for url in child_urls:
                            if not url in url_dict:
                                # print('Pushing',url)
                                url_dict[url] = 1
                                urls.append(url)


    def post_process(self):
        """ Post processing of data """
        
        print('\n\nCrawl complete.')
        print('Fetched',self.count,'URLs.')
        # Dump data
        filename = 'data_%s.pkl' % self.domain
        pickle.dump(self.data_map, open(filename,'wb'))
        print('Data saved to',filename)

        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A simple web crawler using concurrent futures')
    parser.add_argument('url',help='URL to crawl')
    parser.add_argument('-d','--directory',help='Crawl as directory', action='store_true')
    parser.add_argument('-t','--threads',help='Use threads instead of processes', action='store_true')  
    parser.add_argument('-c','--concurrency',help='Concurrency in terms of # of workers', type=int, default=5)

    args = parser.parse_args()
    
    print('Crawling',args.url,'with directory option=',args.directory,'...')
    crawler = Crawler(args.url, directory=args.directory, concurrency=args.concurrency, threads=args.threads)
    crawler.crawl()
    crawler.post_process()
