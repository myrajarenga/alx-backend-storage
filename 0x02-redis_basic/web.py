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


"""Test the get_page function"""
if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.example.com"
    start_time = time.time()
    content = get_page(url)
    end_time = time.time()
    print("Content:")
    print(content)
    print(f"Time taken: {end_time - start_time} seconds")

    time.sleep(2)

    """Access the same URL again"""
    start_time = time.time()
    content = get_page(url)
    end_time = time.time()
    print("Content (cached):")
    print(content)
    print(f"Time taken (cached): {end_time - start_time} seconds")

    """Access the same URL again after cache expiration"""
    time.sleep(8)
    start_time = time.time()
    content = get_page(url)
    end_time = time.time()
    print("Content (after cache expiration):")
    print(content)
    print(f"Time taken (after cache expiration): {end_time - start_time} seconds")
