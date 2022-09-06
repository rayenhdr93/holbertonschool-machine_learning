#!/usr/bin/env python3
''' Error Analysis '''


import numpy as np


def sensitivity(confusion):
    tp = np.diagonal(confusion)
    tpfn = np.sum(confusion, axis=1)
    return (tp / tpfn)
