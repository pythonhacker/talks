""" Prime number generation """

import random
from itertools import cycle,imap,dropwhile,takewhile

def is_prime(n):
    """ Is the number 'n' prime ? """        
    prime = True
    for i in range(2,int(pow(n,0.5))+1):
        if n % i==0: 
            prime = False
            break
    return prime
    
def prime_solution_a(n):

    count, numbers = 0, []

    while count<n:
        num = random.randrange(1,1000)
        if num not in numbers and is_prime(num):    
            numbers.append(num)
            count += 1

    return numbers

def prime_solution_b(n):

    sieve = lambda n: not any(n % num==0 for num in range(2, int(pow(n,0.5))+1))
    nums = set()

    for i in takewhile(lambda x:len(nums)<=20,
                       dropwhile(sieve,imap(random.randrange,cycle([1]),
                                            cycle([100])))):
        nums.add(i)

    return nums

if __name__ == "__main__":
    print prime_solution_a(20)
    print prime_solution_b(20)  
