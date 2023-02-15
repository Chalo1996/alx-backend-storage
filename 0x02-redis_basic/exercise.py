#!/usr/bin/env python3
"""exercise module."""

import redis
import uuid
from typing import BinaryIO


class Cache:
    """Cache class."""
    def __init__(self):
        """init method."""
        __r = redis.Redis()
        self._redis = __r
        self._redis.flushdb()

    def store(self, data: BinaryIO) -> str:
        """store method."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return (key)
