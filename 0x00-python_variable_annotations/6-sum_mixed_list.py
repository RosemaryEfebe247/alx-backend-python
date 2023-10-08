#!/usr/bin/env python3
"""
This type annotated function takes
input in int and float and return sun of float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """Function takes mixed list of int and float
    returns sum in float
    """
    return sum(mxd_lst)
