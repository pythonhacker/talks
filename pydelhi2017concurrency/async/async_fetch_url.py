""" Fetch a URL and process its response using async io """

import asyncio
import aiohttp
import io

async def fetch_page(url):
    """ Asynchronous URL fetcher """
    
    future = aiohttp.request('GET', url)
    # Wait for the future
    response = await future
    
    return response

async def parse_response(done):
    """ Parse responses of fetch """
    
    for future in done:
        response = future.result()
        data = await response.read()
        print('Response for URL',response.url,'=>', response.status, len(data))
        response.close()
        
loop = asyncio.get_event_loop()
urls = ('http://www.google.com',
        'http://www.yahoo.com',
        'http://www.facebook.com',
        'http://www.reddit.com',
        'http://www.twitter.com')


tasks = map(fetch_page, urls)
# Wait for futures
done, pending = loop.run_until_complete(asyncio.wait(tasks, timeout=120))
# Wait for response processing
loop.run_until_complete(parse_response(done))
loop.close()

    


    
