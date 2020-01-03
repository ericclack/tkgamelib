import timeit

CACHE = {}

def cache(fn):
    def wrapper(n):
        if n in CACHE:
            return CACHE[n]
        else:
            v = CACHE[n] = fn(n)
            return v
    return wrapper

@cache
def isprime(n):
    i = 2
    while i < n//i:
        if n % i == 0:
            return False
        i += 1
    return True

def gap(m, n, g):
    last_prime = None
    primes = []
    if m % 2 == 0:
        m += 1
        if m == 2:
            last_prime = 2
            
    for i in range(m, n, 2):
        if isprime(i):
            if last_prime and i-last_prime == 2:
                primes.append([last_prime, i])
            else:
                last_prime = i
    return primes

t = timeit.timeit('print(gap(2, 10000, 2))', number=5, globals=globals())
print()
print(t)
