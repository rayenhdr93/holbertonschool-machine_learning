#!/usr/bin/env python3
''' Error Analysis '''


import numpy as np


def f1_score(confusion):
    tp = np.diagonal(confusion)
    fn = np.sum(confusion, axis=1) - tp
    fp = np.sum(confusion, axis=0) - tp
    return (tp/(tp + 0.5 * (fp + fn)))
