#!/usr/bin/env python3
"""exercise module."""

import redis
import uuid
from typing import IO


class Cache:
    """Cache class."""
    def __init__(self):
        """init method."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: IO[bytes]) -> str:
        """store method."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return (key)
