"""Tools for reducing the braid."""  

import braids
import numpy as np
from braids import *  

def ispermitted(handle):
    """Checks if a handle is permitted."""
    flag = True
    w = handle.word
    j = abs(w[0])
    if j+1 in set(w[1:-1]) and -1*j-1 in set(w[1:-1]):
        flag = False
        # print("Not permitted")
    return flag

def free_reduce(beta):
    """Freely reduces a word and then returns."""
    w = beta.word
    n = len(w)
    for i in range(n-1):
        if w[i]+w[i+1]==0:
            w[i]=0
            w[i+1]=0
    return braid(w)
    
def zero_reduce(beta):
    """Removes all empty letters in a word."""
    w = np.array(beta.word)
    a = w[w!=0]
    return braid(a.tolist())

def double(beta):
    pass

def rnd_new(n):
    """Returns random braid word of length n."""
    pass
    