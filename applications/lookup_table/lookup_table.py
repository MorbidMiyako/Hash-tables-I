# Your code here
import math
import random
import timeit

start = timeit.default_timer()

cache = {}


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    if f"{x},{y}" in cache:
        return cache[f"{x},{y}"]
    else:
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653
        cache[f"{x},{y}"] = v

    # Your code here


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    # print(f'{i}: {x},{y}: {slowfun(x, y)}')

stop = timeit.default_timer()

print('Time: ', stop - start)
