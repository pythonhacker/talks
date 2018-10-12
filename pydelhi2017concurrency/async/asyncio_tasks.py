""" Co-operative multitasking example ported to asyncio """

import asyncio
import time

def number_generator(m, n):
    """ A number generator co-routine in range(m...n+1) """
    yield from range(m, n+1)
    
# @asyncio.coroutine
# async
async def prime_filter(m, n):
    """ Prime number co-routine """
    
    primes = []
    for i in number_generator(m, n):
        if i % 2 == 0: continue
        flag = True

        for j in range(3, int(i**0.5+1), 2):
            if i % j == 0:
                flag = False
                break

        if flag:
            print('Prime=>',i)
            primes.append(i)

        # Uncomment this out and comment next line and see what happens !!!
        await asyncio.sleep(1.0)

        # time.sleep(1)         
        
    return tuple(primes)

async def square_mapper(m, n):
    """ Square mapper co-routine """
    
    squares = []
    for i in number_generator(m, n):
        print('Square=>',i*i)       
        squares.append(i*i)
        # Uncomment this out and comment next line and see what happens !!!
        await asyncio.sleep(1.0)
        # time.sleep(1)
        
    return squares

def print_result(future):
    print('Result=>',future.result())
        
loop = asyncio.get_event_loop()
future = asyncio.gather(prime_filter(10, 50), square_mapper(10, 50))
future.add_done_callback(print_result)
loop.run_until_complete(future)

loop.close()


