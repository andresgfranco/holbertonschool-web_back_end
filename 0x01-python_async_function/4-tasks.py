#!/usr/bin/env python3
"""This module contains the corrutine wait_random"""
import asyncio
import random
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """waits for a random delay between 0 and max_delay"""
    new_list: List[float] = []
    new_list2: List[float] = []

    for i in range(n):
        new_list.append(task_wait_random(max_delay))

    for i in asyncio.as_completed(new_list):
        num: float = await i
        new_list2.append(num)

    return new_list2
