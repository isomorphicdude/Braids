"""Testing algorithm performance."""  # noqa

# If you are using Jupyter notebook()
# Uncomment the following and set chdir to the directory of braids package
# import os
# os.getcwd()
# os.chdir('')
# print(os.getcwd())

import braids
import random
import time
import timeit
from braids import *
import matplotlib.pyplot as plt


def timer_func(func):
    """Returns function for benchmark."""

    def function_timer(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        msg = "{func} took {time} seconds to complete."
        print(msg.format(func = func.__name__,time = runtime))
        return (value, runtime)

    return function_timer

@timer_func
def test_dehornoy(n,l,ntime=10):
    """Create input w of length n and run dehornoy(w)"""
    for i in range(ntime):
        w = rnd_new(n,l)
        dehornoy(w,1000)  

"""Client code"""

# Run tests on varying lengths of words

n = 3

llst = [2**i for i in range(1, 14)]
ltime = [] # list of times
for l in llst:
    ltime.append(test_dehornoy(n,l)[1])
ltime = np.array(ltime)
ltime = ltime[ltime!=0]
print(ltime)  # print

# attampt to smooth
from scipy.signal import savgol_filter
plt.plot(np.arange(len(ltime)), ltime)  
yhat = savgol_filter(ltime, 5, 3) # window size 5, polynomial order 3
plt.plot(np.arange(len(ltime)), yhat)