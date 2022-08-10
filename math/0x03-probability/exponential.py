#!/usr/bin/env python3
''' Exponential calc '''


class Exponential:
    ''' Exponential calc '''

    def __init__(self, data=None, lambtha=1.):
        ''' Initialize Exponential '''
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
            self.lambtha = 1 / (totdata / len(data))

    def pdf(self, x):
        ''' Exponential PDF '''
        e = 2.7182818285
        if x < 0:
            return 0
        pdf = self.lambtha * e ** (- self.lambtha * x)
        return(pdf)
