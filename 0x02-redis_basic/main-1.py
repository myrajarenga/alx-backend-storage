#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache

# Create an instance of the Cache class
cache = Cache()

# Store b"foo" in the cache
key = cache.store(b"foo")

# Test get without callable for b"foo"
value = cache.get(key)
print("Value for b'foo' without callable:", value)  # Output: Value for b'foo' without callable: b'foo'

# Test get with int callable for b"foo" (should raise ValueError)
try:
    value = cache.get(key, fn=int)
    print("Value for b'foo' with int callable:", value)
except ValueError as e:
    print("Caught ValueError:", e)
