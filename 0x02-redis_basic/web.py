#!/usr/bin/env python3
"""
Implementing a get_page function
(prototype: def get_page(url: str) -> str:)
The core of the function is very simple. It uses the requests module
to obtain the HTML content of a particular URL and returns it
"""


import requests
import redis
import time
from typing import Optional


def get_page(url: str) -> str:
    """ function to Create a Redis client"""
    r = redis.Redis()
    cached_content = r.get(url)
    if cached_content is not None:
        return cached_content.decode("utf-8")

    """"Fetch the HTML content from the URL"""
    response = requests.get(url)
    content = response.text

    r.setex(url, 10, content)

    r.incr(f"count:{url}")

    return content
