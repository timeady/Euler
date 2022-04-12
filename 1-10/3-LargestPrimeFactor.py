"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math
from functools import reduce
from timeit import default_timer as timer

start = timer()


def factors(n):
    return max(filter(lambda num: all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)),
                      reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0))))


print(f"Comically long single line = {factors(600851475143)}")
end = timer()
print(end - start)

init_start = timer()


def initial(n):
    factor = 2
    last_factor = 1
    while n > 1:
        if n % factor == 0:
            last_factor = factor
            n = n // factor
            while n % factor == 0:
                n = n // factor
        factor += 1
    return last_factor


print(f"Euler initial = {initial(600851475143)}")
init_end = timer()
print(init_end - init_start)

imp_start = timer()


def refactor_1(n):
    if n % 2 == 0:
        n = n // 2
        last_factor = 2
        while n % 2 == 0:
            n = n // 2
    else:
        last_factor = 1

    factor = 3
    while n > 1:
        if n % factor == 0:
            n = n // factor
            last_factor = factor
            while n % factor == 0:
                n = n // factor
        factor = factor + 2
    return last_factor


print(f"Euler improved = {refactor_1(600851475143)}")
imp_end = timer()
print(imp_end - imp_start)

final_start = timer()


def refactor_2(n):
    if n % 2 == 0:
        last_factor = 2
        n //= 2
        while n % 2 == 0:
            n //= 2
    else:
        last_factor = 1
    factor = 3
    max_factor = n ** 0.5
    while n > 1 and factor <= max_factor:
        if n % factor == 0:
            n //= factor
            last_factor = factor
            while n % factor == 0:
                n //= factor
            max_factor = n ** 0.5
        factor += 2
    if n == 1:
        return last_factor
    else:
        return n


print(f"Final Euler = {refactor_2(600851475143)}")
final_end = timer()
print(final_end - final_start)
