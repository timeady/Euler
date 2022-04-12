"""
If we list all the natural numbers below 10
that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
from timeit import default_timer as timer


def multiples(n):
    return sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0)


init_start = timer()
print(f"Iteration result = {multiples(1000)}")
init_end = timer()
print(init_end - init_start)


def multiples_ref(n, t):
    p = t // n
    return (n * (p * (p + 1))) // 2


def multiples_3_or_5(t):
    three = multiples_ref(3, t)
    five = multiples_ref(5, t)
    fifteen = multiples_ref(15, t)
    return three + five - fifteen


ref_start = timer()
print(f"Refactor = {multiples_3_or_5(999)}")
ref_end = timer()
print(ref_end - ref_start)


