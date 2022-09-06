#!/usr/bin/env python3
''' Error Analysis '''


import numpy


def specificity(confusion):
    tp = numpy.diagonal(confusion)
    tpfn = numpy.sum(confusion, axis=1)
    fp = numpy.sum(confusion, axis=0) - tp
    tn = numpy.sum(confusion) - (tpfn + fp)
    return (tn/(tn+fp))
