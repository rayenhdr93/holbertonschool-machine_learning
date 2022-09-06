#!/usr/bin/env python3
''' Error Analysis is here'''


import numpy as np


def create_confusion_matrix(labels, logits):
    return (np.matmul(labels.T, logits))
