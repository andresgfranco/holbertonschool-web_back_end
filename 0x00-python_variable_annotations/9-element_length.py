#!/usr/bin/env python3
"""This module contains the function element_length
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """only a function that make something :v"""
    return [(i, len(i)) for i in lst]
