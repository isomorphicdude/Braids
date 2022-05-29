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
    
    def __str__(self):
        pass

    def isreduced(self):
        """Checks if word is reduced."""
        pass

    def maingen(self):
        """Returns the main generator. (min index)"""
        a = self.word[0]
        for i in range(self.word):
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




    

        

