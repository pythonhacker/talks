""" Simple web crawler using multiprocessing """

import multiprocessing
import argparse
from concurrent_crawler import Crawler

class MpCrawler(Crawler):
    """ Web crawler using multiprocessing """

    def crawl(self):
        """ Crawl a site recursively """

        urls = [self.url]
        url_dict = {}
        url_dict[self.url] = 1

        pool = multiprocessing.Pool(self.concurrency)
        
        while len(urls):
            results = pool.map(self.fetch_url, urls)
            urls = []

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A simple web crawler using multiprocessing')
    parser.add_argument('url',help='URL to crawl')
    parser.add_argument('-d','--directory',help='Crawl as directory', action='store_true')
    parser.add_argument('-c','--concurrency',help='Concurrency in terms of # of workers', type=int, default=5)

    args = parser.parse_args()
    
    print('Crawling',args.url,'with directory option=',args.directory,'...')
    crawler = MpCrawler(args.url, directory=args.directory, concurrency=args.concurrency)
    crawler.crawl()
    crawler.post_process()
