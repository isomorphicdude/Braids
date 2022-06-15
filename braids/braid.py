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


    def maingen(self):
        """Returns the main generator as integer."""
        w = np.array(self.word)
        m = abs(w)
        return min(m)

    def mainhandle(self):
        """Returns main handle of the word.(if there are multiple, return leftmost one)"""
        out = None
        j = self.maingen()
        if j in self.word and -1*j in self.word:
            pos = self.word.index(j)
            neg = self.word.index(-1*j)
            if pos > neg:
                out = braid(self.word[neg:pos+1])
            else:
                out = braid(self.word[pos:neg+1])
            if not self.ispermitted(out):
                out = "Handle found is not permitted"
            return out
        else:
            print("No main handle found, fully reduced")

    def isreduced(self):
        """Checks if word is reduced."""
        if not self.mainhandle():
            # no main handle returns true
            return True
        else:
            return False

    def left_handle(self):
        """
        Returns the leftmost handle in a word and its start&end.
        
        Parameters:
            - braid: braid type
        Returns:
            - (braid,x,y): a tuple of 3 elements, first being braid, x,y are integers
        """
        w = self.word
        n = len(w)
        j = n
        k = 0
        assert not self.isreduced()

        for i in range(n):
            x = w[i]
            if -1*x in w[i:j]:
                if self.word.index(-1*x)<j:
                    j = self.word.index(-1*x)+1
                    k = i
                    # print(f"k is {i}")
                    # print(f"j is {j}")
        if (j+1)<=n-1:
            out = (w[k:j],k,j)
            # print(k)
        else:
            out = (w[k:-1],k,-1)
            # print(k)
        return (braid(out[0]),out[1],out[2])


    def permutation(self):
        """The permutation to which a braid in [0,1] corresponds."""
        pass



    

        

