#!/usr/bin/env python3
"""exercise module."""


import redis
import uuid
from typing import Union, Callable, Optional


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

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generates a random key and stores the data in the redis\
            server.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
