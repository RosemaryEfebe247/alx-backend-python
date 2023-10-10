#!/usr/bin/env python3
"""
Requirements: Import wait_random from 0-basic_async_syntax.py
Define a function that takes two argument max delay and n
the function returns n times the wait_random functio
return: A list of all delays in ascending order
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Function that returns a list of delays"""
    spawn = []
    for _ in range(n):
        spawn.append(task_wait_random(max_delay))
    result = await asyncio.gather(*spawn)
    return sorted(result)
