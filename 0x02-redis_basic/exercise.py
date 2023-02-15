#!/usr/bin/env python3
"""exercise module."""

import redis
import uuid


class Cache:
    """Cache class."""
    def __init__(self):
        """init method."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: bytes) -> str:
        """store: takes a data argument and returns a string.

        Args:
            data (bytes): data to store.

        Returns:
            str: key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return (key)
