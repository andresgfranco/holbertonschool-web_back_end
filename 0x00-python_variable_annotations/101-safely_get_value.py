#!/usr/bin/env python3
"""This module contains the function safely_get_value
"""


from typing import Union, Mapping, Any, TypeVar


T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, type(None)] = None
        ) -> Union[Any, T]:
    """only a function that make something :v"""
    if key in dct:
        return dct[key]
    else:
        return default
