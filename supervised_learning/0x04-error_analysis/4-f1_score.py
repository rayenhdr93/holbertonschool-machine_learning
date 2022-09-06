#!/usr/bin/env python3
''' Error Analysis '''


import numpy


def f1_score(confusion):
    tp = numpy.diagonal(confusion)
    fn = numpy.sum(confusion, axis=1) - tp
    fp = numpy.sum(confusion, axis=0) - tp
    return (tp/(tp + 0.5 * (fp + fn)))
