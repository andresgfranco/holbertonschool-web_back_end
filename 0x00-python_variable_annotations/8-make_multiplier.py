#!/usr/bin/env python3
"""This module contains the function make_multiplier
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """that takes a float multiplier as argument
        and returns a function that multiplies a float by multiplier.
    """
    def multi(multiplier2: float) -> float:
        """multiplies two numbers"""
        return multiplier * multiplier2

    return multi
