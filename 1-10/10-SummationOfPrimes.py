"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import math
from timeit import default_timer as timer


# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
#
# def summation(n):
#     prime_sum = 0
#     for num in range(2, n):
#         if is_prime(num):
#             prime_sum += num
#     return prime_sum
#
#
# start = timer()
# print(summation(2000000))
# end = timer()
# print(end - start)
#
#
# """
#     Refactors
# """
#
#
# def isPrime(n):
#     if n == 1:
#         return False
#     elif n < 4:
#         return True
#     elif n % 2 == 0:
#         return False
#     elif n < 9:
#         return True
#     elif n % 3 == 0:
#         return False
#     else:
#         r = math.floor(math.sqrt(n))
#         f = 5
#         while f <= r:
#             if n % f == 0:
#                 return False
#             if n % (f + 2) == 0:
#                 return False
#             f = f + 6
#         return True
#
#
# def sums(limit):
#     prime_sum = 5  # 2 and 3 are prime
#     n = 5
#     while n <= limit:
#         if isPrime(n):
#             prime_sum += n
#         n += 2
#         if n <= limit and isPrime(n):
#             prime_sum += n
#         n += 4
#     return prime_sum
#
#
# start = timer()
# print(sums(2000000))
# end = timer()
# print(end - start)


def prime_sieve(n):
    limit = n + 1
    crosslimit = math.floor(math.sqrt(n) - 1) // 2
    sievebound = (n - 1) // 2
    sieve = [False] * n

    for i in range(1, crosslimit):
        if not sieve[i]:
            for j in range((2 * i * (i + 1)), sievebound, 2 * i + 1):
                sieve[j] = True
    sums = 2
    for i in range(1, sievebound):
        if not sieve[i]:
            sums = sums + (2 * i + 1)
    return sums


start = timer()
print(prime_sieve(2000000))
end = timer()
print(end - start)

