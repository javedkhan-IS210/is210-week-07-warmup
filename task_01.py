#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" A function that returns the fibbonacci sequence to a desired limit."""


def fibonacci(maxint):
    """A function return the fibbonacci sequence up to a value

    Args:
        maxint (int):  the upper bound of the sequence.

    Returns:
        list: the fibonacci sequence up to a limit.

    Examples:
        >>> fibonacci(10)
        [0, 1, 1, 2, 3, 5, 8]

        >>> fibonacci(20)
        [0, 1, 1, 2, 3, 5, 8, 13]
    """
    a, b = 0, 1
    myint = [a]
    while b <= maxint:
        myint.append(b)
        a, b = b, a+b
    return myint
