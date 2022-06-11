'''Constructs braid group objects using word'''

import numpy as np
import sympy as sp

class braid(object):

    def __init__(self, word):
        """
        Constructs braid via word.
        - word: a np array of integers e.g. [1,-2,3]=sigma_1 sigma_2^{-1} sigma_3
        """
        self.word = np.array(word)
        self.pos = [] # the positive form using Garside's braid \Delta
    
    def __str__(self):
        return " ".join(str(self.word))

    def __repr__(self):
        return type(self).__name__ + "("+repr(self.word)+")"      

    def isreduced(self):
        """Checks if word is reduced."""
        pass

    def maingen(self):
        """Returns the main generator. (min index)"""
        w = abs(self.word)
        return min(w)

    def mainhandle(self):
        """Returns main handle of the word.(if there are multiple, return leftmost one)"""
        try:
            out = None
            j = self.maingen()
            pos = self.word.index(j)
            neg = self.word.index(-1*j)
            if pos > neg:
                out = self.word[neg:pos+1]
            else:
                out = self.word[pos:neg+1]
            return out
        except :
            raise "No handles found"

    def isreducible(self):
        """Checks if word is permitted."""
        flag = True
        handle = self.handle()
        j = handle[0]
        if j+1 in set(handle[1:-1]) and -1*j-1 in set(handle[1:-1]):
            flag = False
        return flag
        
    def left_handle(self):
        """Returns the leftmost handle in a word."""
        pass

    def permutation(self):
        """The permutation to which a braid in [0,1] corresponds."""




    

        

