#!/usr/bin/env python3
"""Fibonacci"""

def fibonacci_tabulation(n):
    """
    Returns the fibonacci value at n
    using tabulation
    """
    if n in {0, 1}: return n

    seq = [x for x in range(n + 1)]

    seq[0] = 0
    seq[1] = 1
    for i in range(2, n + 1):
        seq[i] = seq[i - 1] + seq[i - 2]

    return seq[n]

def fibonacci(n):
    """
    Returns the fibonacci value at n
    without using tabulation
    """
    if n in {0, 1}: return n

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr

def fibonacci_memo(n):
    """
    Returns the fibonacci value at n
    using memoization
    """
    if n in {0, 1}: return n

    # The current n is equal to n-1 + n-2
    return fibonacci_memo(n - 1) + fibonacci_memo(n - 2)

cache = {}
def fibonacci_memo_cache(n):
    """
    Returns the fibonacci value at n
    using memoization and optimized by caching results
    """
    if n in {0, 1}: return n

    if n not in cache:
        cache[n] = fibonacci_memo_cache(n - 1) + fibonacci_memo_cache(n - 2)

    return cache[n]
