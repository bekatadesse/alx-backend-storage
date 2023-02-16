#!/usr/bin/env python3

"""
Module exercise
"""
import redis
from typing import Union, Optional, Callable
import uuid
from functools import wraps


class Cache:
    """
    A redis Cache class
    """
    def __init__(self):
        """
        Stores an instnace of redis client
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Takes a data argument and
        returns a string
        """
        key: uuid.UUID = str(uuid.uuid1())

        self._redis.set(key, data)

        return key

    def get(self,
            key: str,
            fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float]:
        """
        Read from redis and
        recover original type
        """
        data = self._redis.get(key)

        return fn(data) if fn else data

    def get_str(self, data: bytes) -> str:
        """
        convert bytes to string
        """
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """
        convert string to integer
        """
        return int(data)
