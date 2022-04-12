"""
By listing the first six prime numbers:
2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import math
from timeit import default_timer as timer


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def nthPrime(n):
    num_of_primes = 0
    prime = 1

    while num_of_primes < n:
        prime += 1
        if isPrime(prime):
            num_of_primes += 1
    return prime


init_start = timer()
print(nthPrime(10001))
init_end = timer()
print(init_end - init_start)



"""
    Refactor
"""


def isPrime(n):
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r = math.floor(math.sqrt(n))
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f = f + 6
        return True


def n_prime(n):
    count = 1
    candidate = 1
    while count != n:
        candidate = candidate + 2
        if isPrime(candidate):
            count += 1
    return candidate


start = timer()
print(n_prime(10001))
end = timer()
print(end - start)
