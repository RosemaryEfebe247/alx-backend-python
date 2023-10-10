#!/usr/bin/env python3
"""
This function is an asynchronous function
Its takes in an int or a float and delays for a period from 0-int
returns the int
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Args:
        max_delay: integer value of input set to default 10
    delay:
        Generates random number of int or float
        delay for a duration between 0 and max_delay
    return:
        return the random number
    """
    rand_num = random.uniform(0, max_delay)
    await asyncio.sleep(rand_num)
    return rand_num
