'''Constructs braid group objects using word'''

import numpy as np

class braid(object):

    def __init__(self, word):
        """
        Constructs braid via word.
        - word: a np array of integers e.g. [1,-2,3]=sigma_1 sigma_2^{-1} sigma_3
        """
        self.word = word
        # self.pos = [] # the positive form using Garside's braid \Delta
    
    def __str__(self):
        return " ".join(str(self.word))

    def __repr__(self):
        return type(self).__name__ + "("+repr(self.word)+")"      

    def isreduced(self):
        """Checks if word is reduced."""
        

    def maingen(self):
        """Returns the main generator. (min index)"""
        w = np.array(self.word)
        m = abs(w)
        return np.argmin(m)

    def mainhandle(self):
        """Returns main handle of the word.(if there are multiple, return leftmost one)"""
        out = None
        j = self.maingen()
        if j in self.word and -1*j in self.word:
            pos = self.word.index(j)
            neg = self.word.index(-1*j)
            if pos > neg:
                out = self.word[neg:pos+1]
            else:
                out = self.word[pos:neg+1]
            if not self.isreducible(out):
                print("Not permitted")
            return out
        else:
            print("No main handle found, fully reduced")

    def isreducible(self, handle):
        """Checks if a handle is permitted."""
        flag = True
        j = abs(handle[0])
        if j+1 in set(handle[1:-1]) and -1*j-1 in set(handle[1:-1]):
            flag = False
            print("Not permitted")
        return flag
        
    def left_handle(self):
        """Returns the leftmost handle in a word."""

         

    def permutation(self):
        """The permutation to which a braid in [0,1] corresponds."""
        pass



    

        

