#!/usr/bin/env python3
import asyncio
import random
from typing import Union

async def wait_random(max_deplay: int = 10) -> int:
    deplay = random.uniform(0, max_deplay)
    await asyncio.sleep(deplay)
    return deplay