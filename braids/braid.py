'''Constructs braid group objects using word'''

import numpy as np
import sympy as sp

class braid(object):

    def __init__(self, word):
        """
        Constructs braid via word.
        - word: a np array of integers e.g. [1,-2,3]=sigma_1 sigma_2^{-1} sigma_3
        """
        self.word = word
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
        a = self.word[0]
        for i in range(len(self.word)):
            m = self.word[i]
            if abs(m)<a and -1*m in self.word:
                a = m
        return a

    def mainhandle(self):
        """Returns main handle of the word."""
        j = self.maingen()
        

    def isreducible(self):
        """Checks if word is permitted."""
        flag = True
        handle = self.handle()
        j = handle[0]
        if j+1 in set(handle[1:-1]) and -1*j-1 in set(handle[1:-1]):
            flag = False
        return flag
        
    def handle(self):
        """Returns the outermost handle in a word."""
        pass




    

        

