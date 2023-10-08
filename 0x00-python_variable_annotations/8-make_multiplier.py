#!/usr/bin/env python3
""" The function takes a multiplier in float
returns a function that multipliers a float by a multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function that returns a function of a multiplier
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
