from concurrent.futures import ProcessPoolExecutor
import requests

urls = ('http://www.google.com',
        'http://www.yahoo.com',
        'http://www.facebook.com',
        'http://www.reddit.com',
        'http://www.twitter.com')

def fetch_url(url):
    response = requests.get(url)
    return (response.url, response.status_code, response.text)
    
        
with ProcessPoolExecutor(max_workers=5) as executor:
    results = executor.map(fetch_url, urls, timeout=120)
    print(results)
    for result in results:
        url, status, data = result
        print('Response for URL',url,'=>', status, len(data))       

