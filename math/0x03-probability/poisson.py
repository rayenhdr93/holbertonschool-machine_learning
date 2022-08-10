#!/usr/bin/env python3
'''pep 8'''


class Poisson:
    ''' poisson '''

    def __init__(self, data=None, lambtha=1.):
        '''doc'''
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            totdata = 0
            for x in data:
                totdata = totdata + x
            self.lambtha = totdata / len(data)

    def pmf(self, k):
        '''doc'''
        e = 2.7182818285
        if type(k) is not int:
            k = int(k)
        if k < 0:
            return(0)
        fac = 1
        for i in range(k, 0, -1):
            fac = fac * i
        pmf = (e ** (-self.lambtha) * self.lambtha ** k) / fac
        return(pmf)

    def cdf(self, k):
        e = 2.7182818285
        if type(k) is not int:
            k = int(k)
        if k < 0:
            return(0)
        cdf = 0
        for i in range(0, k + 1):
            cdf = cdf + self.pmf(i)
        return(cdf)
