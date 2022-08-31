#!/usr/bin/env python3
'''Neuron is here'''


import numpy as np


class Neuron:
    '''Neuron is here'''
    def __init__(self, nx):
        if type(nx) is not int:
            raise TypeError('nx must be an integer')
        if nx < 1:
            raise ValueError('nx must be a positive integer')
        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        return self.__W

    @property
    def b(self):
        return self.__b

    @property
    def A(self):
        return self.__A

    def forward_prop(self, X):
        '''Neuron is here'''
        product = np.matmul(self.W, X)
        x = product + self.__b
        self.__A = 1.0/(1.0 + np.exp(-x))
        return(self.__A)
