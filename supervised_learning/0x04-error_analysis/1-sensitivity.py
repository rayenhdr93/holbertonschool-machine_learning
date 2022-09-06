#!/usr/bin/env python3
''' Error Analysis '''


import numpy


def sensitivity(confusion):
    tp = numpy.diagonal(confusion)
    tpfn = numpy.sum(confusion, axis=1)
    return (tp / tpfn)
