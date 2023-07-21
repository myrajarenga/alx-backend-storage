#!/usr/bin/env python3
"""
Writing strings to Redis
"""


import redis
import uuid
from typing import Union, Callable
import functools


class Cache:
    def __init__(self):
        """sore an instance of redis as private"""
        self._redis = redis.Redis()

        """flush the instance"""
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate random key using UUID"""
        key = str(uuid.uuid4())

        """store input in redis using rando keym"""
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Callable = None)\
            -> Union[str, bytes, int, float]:
        """retrive data from redis"""
        data = self._redis.get(key)

        if data is None or fn is None:
            return data

            return fn(data)

    def get_str(self, key: str) -> str:
        """method to get value as UTF8"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """methid to get value as integer"""
        return self.get(key, fn=int)

    def count_calls(self, method: Callable) -> Callable:
        """define function that waraps args"""
        @functools.wraps(method)
        def wrapper(*args, **kwargs):
            """get name for the method"""
            method_name = method.__qualified__
            self._redis.incr(methid_name)

            return method(*args, **kwargs)
        return wrapper
