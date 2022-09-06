#!/usr/bin/env python3
''' Error Analysis is here'''


import numpy


def create_confusion_matrix(labels, logits):
    return (numpy.matmul(labels.T, logits))
