#!/usr/bin/env python3
"""This module contains the measure_time function"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time for wait_n(n, max_delay)"""
    start_time = time.time()

    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()
    total = end_time - start_time

    return total / n
