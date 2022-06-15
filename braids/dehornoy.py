"""Implements Dehornoy's algortihm"""   

from braids import braid
import numpy as np
from braids import reduction_tools

def HR(handle):
    """Reduces and returns a handle."""
    # length preserving
    assert braid.ispermitted(handle)

    h = handle.word
    j = h[0] # first element
    assert j!=0
    e = j//abs(j) # sign of exponent
    
    # apply transformation
    h[0] = 0
    h[-1] = 0
    k = None
    m = abs(j)+1 # j+1 generator
    if m in h:
        k = h.index(abs(j)+1)
        f = 1
    elif -1*m in h:
        k = h.index(-abs(j)-1)
        f = -1
    if k:
        h[k:(k+1)] = [-1*e*m,f*abs(j),e*m]
    return braid(h)

def dehornoy(beta):
    # pseudo-code

    # while not fully reduced:
    #   find leftmost handle
    #   reduce using map(in place?)
    #   free_reduce(whole word)
    #   (note this is always permitted as it ends at the leftmost)
    cnt = 0
    while not beta.isreduced():
        output = beta.left_handle()
        handle = output[0]
        k = output[1] # start
        j = output[2] # end
        h = handle.word
        assert h # assert not non-empty
        beta[k:j] = HR(handle=handle)
        cnt += 1
        # print verbose
        match cnt:
            case 10:
                print("10 already")
            case 100:
                print("100 already")
            case 1000:
                print("1000 already")
                

