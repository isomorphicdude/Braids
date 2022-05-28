'''Constructs braid group objects using word'''

class braid(object):

    def __init__(self, word):
        """
        Constructs braid via word.
        - word: a list of integers e.g. [1,-2,3]=sigma_1 sigma_2^{-1} sigma_3
        """
        self.word = word
    
    def __str__(self):
        pass

    def isreduced(self):
        """Checks if word is reduced."""
        pass

    def maingen(self):
        """Returns the main generator. (min index)"""
        pass
    def isreducible(self):
        """"""
        pass

        

