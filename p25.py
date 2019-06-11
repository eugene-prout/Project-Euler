from functools import lru_cache
import sys
from timeit import default_timer as timer


@lru_cache(maxsize=None)
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

class recursionlimit:
    def __init__(self, limit):
        self.limit = limit
        self.old_limit = sys.getrecursionlimit()

    def __enter__(self):
        sys.setrecursionlimit(self.limit)

    def __exit__(self, type, value, tb):
        sys.setrecursionlimit(self.old_limit)

with recursionlimit(10000):
    start = timer()
    for x in range(1,1000000):
        y = fib(x)
        if len(str(y)) > 9999:
            print(x)
            break
    end = timer()

print("Time taken:", end-start, "s")
        