#!/usr/bin/env python3
"""
Writing strings to Redis
"""


import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        """sore an instance of redis as private"""
        self._redis = redis.Redis()

        """flush the instance"""
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float] -> str):
        """generate random key using UUID"""
        key = str(uuid.uuid4())

        """store input in redis using rando keym"""
        self._redis.set(key, data)

        return key
