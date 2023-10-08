#!/usr/bin/env python3
"""
The function takes a list of strings
Returns a tupple of lists
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in the input list
    Args:
        lst (List[str]): The input list of strings.
    Returns:
        List[Tuple[str, int]]: A list of tuples
    """
    return [(i, len(i)) for i in lst]
