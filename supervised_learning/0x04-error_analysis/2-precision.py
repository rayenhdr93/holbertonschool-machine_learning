#!/usr/bin/env python3
''' Error Analysis '''


import numpy as np


def precision(confusion):
    ''' Error Analysis '''
    tp = np.diagonal(confusion)
    tpfp = np.sum(confusion, axis=0)
    return (tp / tpfp)
