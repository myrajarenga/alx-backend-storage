#!/usr/bin/env python3
"""
Writing strings to Redis
"""


import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(self, method: Callable) -> Callable:
    """return a callable function"""
    method_name = method.__qualname__

    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        """get wrapper for decorated function"""
        self._redis.incr(method_name)

        return method(self, *args, **kwargs)

    return wrapper


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

    def get(self, key: str, fn: Optional[callable] = None) \
            -> Union[str, bytes, int, float]:
        """convert the data back to the desired format"""
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """automatically parametrize Cache.get with the correct
        conversion function"""
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        """automatically parametrize Cache.get with the correct
        conversion function"""
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value = 0
        return value
