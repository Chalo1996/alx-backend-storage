#!/usr/bin/env python3
"""exercise module."""

import redis
import uuid
from typing import Union, Callable


class Cache:
    """Cache class."""

    def __init__(self):
        """init method."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store: takes a data argument and returns a string.

        Args:
            data (bytes): data to store.

        Returns:
            str: key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return (key)

    def get(self,
            key: str,
            fn: callable = None) -> Union[str,
                                          bytes,
                                          int,
                                          float]:
        """get: takes a key string argument and an optional
        Callable argument named fn.

        Args:
            key (str): key.
            fn (callable, optional): function. Defaults to None.

        Returns:
            Union[str, bytes, int, float]: data.
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """get_str: takes a key string argument and returns the
        string value stored in Redis.

        Args:
            key (str): key.

        Returns:
            str: data.
        """
        data = self._redis.get(key)
        return data.decode('utf-8')

    def get_int(self, key: str) -> int:
        """get_int: takes a key string argument and returns the
        integer value stored in Redis.

        Args:
            key (str): key.

        Returns:
            int: data.
        """
        data = self._redis.get(key)
        return int(data.decode('utf-8'))
