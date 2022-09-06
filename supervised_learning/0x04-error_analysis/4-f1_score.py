#!/usr/bin/env python3
''' Error Analysis '''


import numpy as np
sensitivity = __import__('1-sensitivity').sensitivity
precision = __import__('2-precision').precision


def f1_score(confusion):
    ''' Error Analysis '''
    r = sensitivity(confusion)
    p = precision(confusion)
    return (2 * ((p * r) / (p + r)))
