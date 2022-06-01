class RangeError:
    pass

class Braid:
    """ A Braid group. """

    def __init__(self, n):
        """
        n: number of strings, i.e. construct a B_n braid group.
        """
        
        self.n = n
        printstr = ''
        for i in range(self.n):
            printstr += '| '
        self.prtunit = printstr
        self.oplist = []

    def op(self, i):
        """
        i: swap ith and (i+1)th string with ith string under (i+1)th
        enter minus value to make inverse.
        """
        
        self.oplist.append(i)
        self.pn_huajian()

    def paixu(self):
        for i in range(len(self.oplist)):
            pass

    def pn_huajian(self):
        
        """
        If \sigma_n and \sigma_{-n} are next to each other, then cancel them.
        """
        for j in range(len(self.oplist)-1):
            if self.oplist[j] + self.oplist[j+1] == 0:
                self.oplist.pop(j)
                self.oplist.pop(j)

    def oto_huajian(self):
        """
        If 
        """
        pass
    
    def __str__(self):
        prt = [self.prtunit]
        for i in self.oplist:
            ai = abs(i)
            line = ''
            for j in range(ai-1):
                line += '| '
            line1 = line + '\ / '
            line3 = line + '/ \ '
            if i > 0:
                line2 = line + ' /  '
            else:
                line2 = line + ' \  '
            line = ''
            for j in range(self.n-ai-1):
                line += '| '
            line1 += line
            line2 += line
            line3 += line
            prt.append(line1)
            prt.append(line2)
            prt.append(line3)
            prt.append(self.prtunit)
        to_be_print = ''
        for k in prt:
            to_be_print += k
            to_be_print += "\n"
        return to_be_print
