#!/usr/bin/env python3
"""This mudole contyains the measure_runtime function"""


import asyncio
import random
import time
from typing import Generator


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """returns the 10 random numbers."""
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end_time = time.time()
    return end_time - start_time
