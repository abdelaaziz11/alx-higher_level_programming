#!/usr/bin/python3
"""Module lazy_matrix_mul
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Multiplies m_a and m_b using matmul
    """
    return numpy.matmul(m_a, m_b)
