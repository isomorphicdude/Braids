"""Testing algorithm performance."""  # noqa

import braids
import random
import time
import timeit
from braids import *


def timer_func(func):
    """Returns function for benchmark."""

    def function_timer(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        msg = "{func} took {time} seconds to complete."
        print(msg.format(func = func.__name__,time = runtime))
        return value

    return function_timer

@timer_func
def test_dehornoy(n,l):
    """Create input w of length n and run dehornoy(w)"""
    w = rnd_new(n,l)
    dehornoy(w)


if __name__ == '__main__':
    n = input("Enter the width: \n")
    l = input("Enter the length of the word: \n")
    test_dehornoy(n,l)