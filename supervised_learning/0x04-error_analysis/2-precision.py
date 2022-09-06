#!/usr/bin/env python3
''' Error Analysis '''


import numpy


def precision(confusion):
    tp = numpy.diagonal(confusion)
    tpfp = numpy.sum(confusion, axis=0)
    return (tp / tpfp)
