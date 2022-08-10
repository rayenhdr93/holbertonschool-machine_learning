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

    def pmf(self, k):
        ''' Binomial PMF '''
        if type(k) is not int:
            int(k)
        if k < 0:
            return(0)
        facn = 1
        fack = 1
        facnk = 1
        for x in range(self.n, 0, -1):
            facn = facn * x
        for x in range(k, 0, -1):
            fack = fack * x
        for x in range(self.n - k, 0, -1):
            facnk = facnk * x
        x = facn / (fack * facnk)
        return (x * (self.p ** k) * ((1 - self.p) ** (self.n - k)))

    def cdf(self, k):
        ''' Binomial CDF '''
        if type(k) is not int:
            int(k)
        if k < 0:
            return(0)
        cdf = 0
        for i in range(0, k + 1):
            cdf = cdf + self.pmf(i)
        return(cdf)
