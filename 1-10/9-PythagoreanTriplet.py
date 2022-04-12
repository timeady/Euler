"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import math
from timeit import default_timer as timer


def triplet(s):
    for a in range(1, s):
        for b in range(1, s):
            c = s - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c


start_time = timer()
print(triplet(1000))
end_time = timer()
print(end_time - start_time)


def triples(n):
    for a in range(3, (n - 3) // 3):
        for b in range(a + 1, (n - 1 - a) // 2):
            c = n - a - b
            if c ** 2 == a ** 2 + b ** 2:
                return a * b * c


b_start = timer()
print(triples(1000))
b_end = timer()
print(b_end - b_start)


def triplet_euclid(s):
    for m in range(1, s):
        for n in range(1, int(math.sqrt(s))):
            a = m ** 2 - n ** 2
            b = 2 * m * n
            c = m ** 2 + n ** 2
            if (a + b + c) == s:
                return a * b * c


euc_start = timer()
print(triplet_euclid(1000))
euc_end = timer()
print(euc_end - euc_start)






