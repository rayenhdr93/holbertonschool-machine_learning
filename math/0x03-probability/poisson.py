#!/usr/bin/env python3
'''pep 8'''


class Poisson:
    ''' poisson '''
    def __init__(self, data=None, lambtha=1.):
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