""" Fetch a URL using async IO """
import asyncio
import aiohttp
import io

async def fetch_page(url):
    """ Asynchronous URL fetcher """
    
    future = aiohttp.request('GET', url)
    # Wait for the future
    response = await future
    
    return response
    
loop = asyncio.get_event_loop()
urls = ('http://www.google.com',
        'http://www.yahoo.com',
        'http://www.facebook.com',
        'http://www.reddit.com',
        'http://www.twitter.com')

tasks = map(fetch_page, urls)
# Wait for tasks
done, pending = loop.run_until_complete(asyncio.wait(tasks, timeout=120))
loop.close()

for future in done:
    response = future.result()
    print(response)
    response.close()
    


    
