#!/usr/bin/env python3
''' Binomial calc '''


class Binomial:
    ''' Binomial calc '''

    def __init__(self, data=None, n=1, p=0.5):
        ''' Initialize Binomial '''
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p < 0 or p > 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(round(n))
            self.p = float(p)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            totdata = 0
            for x in data:
                totdata = totdata + x
            mean = totdata / len(data)
            s = 0
            for x in data:
                s = s + ((x - mean) ** 2)
            variance = (s / len(data))
            q = variance / mean
            p = 1 - q
            n = round(mean / p)
            p = mean / n
            self.n = int(n)
            self.p = float(p)
