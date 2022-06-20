"""Implements Dehornoy's algortihm"""   

from braids import braid
import numpy as np
from braids import reduction_tools

def HR(handle: braid):
    """Reduces and returns a handle."""
    # length preserving
    assert braid.ispermitted(braid([0]),handle)

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

def dehornoy(beta, early_termination = 100):
    # pseudo-code

    # while not fully reduced:
    #   find leftmost handle
    #   reduce using map(in place?)
    #   free_reduce(whole word)
    #   (note this is always permitted as it ends at the leftmost)
    cnt = 0
    while not beta.isreduced() and beta.word:
        # debugging
        print(f"Before reduction: {beta.word}")

        reduction_tools.free_reduce(beta)
        reduction_tools.zero_reduce(beta)

        if not beta.word:
            return beta

        output = beta.left_handle()
        handle = output[0]

        # handle reduction
        k = output[1] # start
        j = output[2] # end

        assert handle.word # assert not non-empty

        beta.word[k:j] = HR(handle=handle).word

        # free reduction
        reduction_tools.free_reduce(beta)
        reduction_tools.zero_reduce(beta)

        print(f"After reduction:{beta.word}")
        cnt += 1
        # print verbose
        match cnt:
            case 10:
                print("10 already")
            case 100:
                print("100 already")
            case 1000:
                print("1000 already")
        if cnt>early_termination:
            raise RuntimeError(f"{early_termination} already reached!")
    return beta
                

