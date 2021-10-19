#!/usr/bin/env python3
"""This module contains the corrutine wait_random"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random delay between 0 and max_delay"""
    n = random.uniform(0, max_delay)
    await asyncio.sleep(n)

    return n
