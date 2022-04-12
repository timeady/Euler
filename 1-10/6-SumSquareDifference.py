"""
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the
first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares
 of the first one hundred natural numbers and the square of the sum.
"""
from timeit import default_timer as timer


init_start = timer()
def sum_square(n):
    num_sum = 0
    for i in range(1, n + 1):
        num_sum += i * i
    return num_sum


def square_sum(n):
    sums = 0
    for i in range(1, n + 1):
        sums += i
    return sums ** 2


def sum_square_diff(n):
    return square_sum(n) - sum_square(n)


print(sum_square_diff(100))
init_end = timer()
print(init_end - init_start)


"""
Refactors
"""

brute_start = timer()
def brute(n):
    sum_sq = 0
    sum = 0
    for num in range(1, n + 1):
        sum += num
        sum_sq = sum_sq + num ** 2
    return sum ** 2 - sum_sq


print(brute(100))
brute_end = timer()
print(brute_end - brute_start)


start = timer()
def sum_squares(n):
    sum = n * (n + 1) / 2
    sum_sq = (2 * n + 1) * (n + 1) * n / 6
    return int(sum ** 2 - sum_sq)


print(sum_squares(100))
end = timer()
print(end - start)



