from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    print('calling fibonacci(%d)' % n)
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print([fibonacci(n) for n in range(1, 9)])
