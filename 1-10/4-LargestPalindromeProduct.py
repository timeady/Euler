"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of
two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
from timeit import default_timer as timer
pal_start = timer()


def palindrome():
    curr_max, max_1, max_2 = 0, 0, 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            curr = i * j
            if curr > curr_max:
                s = str(curr)
                if s == s[::-1]:
                    curr_max = curr
                    max_1 = i
                    max_2 = j
    print(f"{max_1} * {max_2}")
    return curr_max


print(palindrome())
pal_end = timer()
print(pal_end - pal_start)

ref_start = timer()


"""
    Refactor
"""
def reverse(n):
    rev = 0
    while n > 0:
        rev = n % 10 + rev * 10
        n //= 10
    return rev


def isPalindrome(n):

    return n == reverse(n)


def largest_pal():
    largest_palindrome = 0
    a = 999
    while a >= 100:
        if a % 11 == 0:
            b = 999
            db = 1
        else:
            b = 990
            db = 11
        while b >= a:
            if a * b <= largest_palindrome:
                break
            if isPalindrome(a*b):
                largest_palindrome = a * b
            b -= db
        a -= 1
    return largest_palindrome


print(largest_pal())
ref_end = timer()
print(ref_end - ref_start)


