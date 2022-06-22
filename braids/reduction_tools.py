"""Tools for reducing the braid."""  

from braids import braid
import numpy as np

def zero_reduce(beta: braid):
    """Removes all empty letters in a word."""
    if beta.word:
        w = np.array(beta.word)
        a = w[w!=0]
        beta.word = a.tolist()
    else:
        beta.word = [0]
        print("Nullstring obtained: identity element.")

def free_reduce(beta: braid):
    """Freely reduces a word and then returns."""
    w = beta.word
    n = len(w)
    for i in range(n-1):
        if w[i]+w[i+1]==0:
            w[i]=0
            w[i+1]=0
    beta.word = w
    
def double(beta):
    pass

def rnd_old(n, l):
    """Returns random braid word of length l."""
    a = (-1)*(n)
    b = n-1
    rnd = np.random.randint(a, b, l)
    return braid(rnd.tolist())

def rnd_new(n, l):
    """Returns random braid of length l width n"""
    rnd = []
    for i in range(l-1):
        if i%2==0:
            rnd.append(np.random.randint(1,n))
        else:
            rnd.append(np.random.randint(1,n)*(-1))
    rnd_temp = np.array(rnd)

    # ensure there is one handle at least
    mingen_ind = np.argmin(abs(rnd_temp))
    
    rnd.append(-1*rnd[mingen_ind])

    return braid(rnd)

    