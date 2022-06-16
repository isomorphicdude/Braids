"""Tools for reducing the braid."""  

from braids import braid
import numpy as np

def zero_reduce(beta):
    """Removes all empty letters in a word."""
    w = np.array(beta.word)
    a = w[w!=0]
    return braid(a.tolist())

def free_reduce(beta):
    """Freely reduces a word and then returns."""
    w = beta.word
    n = len(w)
    for i in range(n-1):
        if w[i]+w[i+1]==0:
            w[i]=0
            w[i+1]=0
    return braid(w)
    
def double(beta):
    pass

def rnd_new(n):
    """Returns random braid word of length n."""
    pass
    