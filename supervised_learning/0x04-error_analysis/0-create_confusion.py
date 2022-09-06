#!/usr/bin/env python3
''' Error Analysis '''


import numpy


def create_confusion_matrix(labels, logits):
    return (numpy.matmul(labels.T, logits))
