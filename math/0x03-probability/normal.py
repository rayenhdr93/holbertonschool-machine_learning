#!/usr/bin/env python3
''' Normal calc '''


class Normal:
    ''' Normal calc '''

    def __init__(self, data=None, mean=0., stddev=1.):
        ''' Initialize Normal '''
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.stddev = float(stddev)
            self.mean = float(mean)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            totdata = 0
            for x in data:
                totdata = totdata + x
            self.mean = (totdata / len(data))
            stdsquare = 0
            for x in data:
                stdsquare = stdsquare + ((x - self.mean) ** 2)
            stdsquare = stdsquare / len(data)
            self.stddev = stdsquare ** 0.5

    def z_score(self, x):
        ''' Normalize Normal '''
        return ((x - self.mean) / self.stddev)

    def x_value(self, z):
        ''' Normalize Normal '''
        return ((z * self.stddev) + self.mean)
