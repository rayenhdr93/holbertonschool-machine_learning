#!/usr/bin/env python3
""" why its not workin"""


def summation_i_squared(n):
    """just why ???"""

    if (type(n) is not int) or (n < 1):
        return None
    if n == 1:
        return n
    else:
        return n**2 + summation_i_squared(n-1)
