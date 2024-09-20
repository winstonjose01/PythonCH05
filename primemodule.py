def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    
def print_primes(n):
    for i in range(n-1):
        if (is_prime(i)):
            print (f'{i} is a prime number\n')
    

def get_primes(n):
    primelst= []
    for i in range(n-1):
        if (is_prime(i)):
            primelst.append(i)
    print (primelst)
    