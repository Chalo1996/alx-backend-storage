#!/usr/bin/env python3
"""exercise module."""


import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


class Cache:
    """Simulates the Caching of redis keys. Creates a new connection\
        everytime an instance of this class is created, saves the\
            keys temporalily, and deletes the keys when the execution of\
                the instance stops.
    """

    def __init__(self):
        """Instantiates a new connection to redis. Flushes the redis\
            server once connection terminates.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def count_calls(method: Callable) -> Callable:
        """Take a function and return a function that counts how many\
            times the function was called.

        Args:
            method (Callable): The function to be wrapped.

        Returns:
            Callable: The wrapped function.
        """
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            key = method.__qualname__
            self._redis.incr(key)
            return method(self, *args, **kwargs)
        return wrapper

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generates a random key and stores the data in the redis\
            server.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable
            = None) -> Union[str, bytes, int, float]:
        """Used to convert data back to desired format."""
        newkey = self._redis.get(key)
        if fn:
            return fn(newkey)
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """Converts data to UTF-8 format."""
        if key:
            return self.get(
                key, lambda d: d.decode("utf-8")
            )

    def get_int(self, key: str) -> int:
        """Converts data to integer format."""
        if key:
            return self.get(
                key, lambda d: int(d.decode("utf-8"))
            )
