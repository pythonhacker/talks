from concurrent.futures import ProcessPoolExecutor

def is_prime(n):
    """ Check for input number primality """
    
    for i in range(3, int(n**0.5+1), 2):
        if n % i == 0:
            print(n,'is not prime')
            return False

    print(n,'is prime')     
    return True

if __name__ == "__main__":
    numbers = [1297337, 1116281, 104395303, 472882027, 533000389, 817504243, 982451653, 112272535095293, 115280095190773, 1099726899285419]*100

    with ProcessPoolExecutor(max_workers=4) as executor:
        future_map = {executor.submit(is_prime, number): number for number in numbers}
        for future in as_completed(future_map):
            number = future_map[future]
            status = future.result()
            if status:
                print('Number',number,'is prime')
            else:
                print('Number',number,'aint prime')        
