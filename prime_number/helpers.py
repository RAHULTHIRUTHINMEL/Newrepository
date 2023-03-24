import constants as c

def is_prime(num):
    if num > 1:
        for n in range(2, num):
            if num % n != 0:
                #keep on checking
                continue
            else:
                return False
            
    return True


def calculate_primes(start, finish):
    primes = []
    for n in range(start,finish):
        if is_prime(n) and n not in c.SKIP_RANGE:   #skip btw 20 and 50
            primes.append(n)
    
    return primes



