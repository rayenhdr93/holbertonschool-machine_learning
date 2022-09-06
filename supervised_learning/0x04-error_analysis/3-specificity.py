#!/usr/bin/env python3
''' Error Analysis '''


import numpy as np


def specificity(confusion):
    tp = np.diagonal(confusion)
    tpfn = np.sum(confusion, axis=1)
    fp = np.sum(confusion, axis=0) - tp
    tn = np.sum(confusion) - (tpfn + fp)
    return (tn/(tn+fp))
