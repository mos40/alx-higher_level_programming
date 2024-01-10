#!/usr/bin/python3
"""
Lazy matrix multiplication using numpy
"""

import numpy


def lazy_matrix_mul(m_a, m_b):
    """Calculates the matrix multiplication"""
    return numpy.matmul(m_a, m_b)
