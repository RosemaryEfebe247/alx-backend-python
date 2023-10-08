#!/usr/bin/env python3
"""
A type annotated function
Return the sum of the array in float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Function that returns the sum of a list
    """
    return sum(input_list)
