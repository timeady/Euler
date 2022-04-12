"""
2520 is the smallest number that can be divided
by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?
"""
from functools import reduce
import math
from timeit import default_timer as timer


bi_start = timer()
def lcm_builtin(*args):
    return math.lcm(*args)


print(lcm_builtin(*range(1, 20)))
bi_end = timer()
print(bi_end - bi_start)


lcm_start = timer()
def lcm(a, b):
    return a * b // math.gcd(a, b)


def lcm_args(*args):
    return reduce(lcm, args)


print(lcm_args(*range(1, 20)))
lcm_end = timer()
print(lcm_end - lcm_start)


"""
    Refactors
"""
ref_start = timer()
def lcm_r():
    a = []
    p = [x for x in range(2, 100) if all(x % m != 0 for m in range(2, x - 1))]
    k = 20
    N = 1
    i = 1
    check = True
    limit = math.sqrt(k)
    while p[i] <= k:
        a.append(1)
        if check:
            if p[i] <= limit:
                a.append(math.floor(math.log(k) / math.log(p[i])))
            else:
                check = False
        N = N * p[i] ** a[i]
        i = i + 1
    print(a)
    print(p)
    return N


print(lcm_r())
ref_end = timer()
print(ref_end - ref_start)