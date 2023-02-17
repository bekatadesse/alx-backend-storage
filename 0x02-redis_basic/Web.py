#!/usr/bin/env python3

"""

Module web

"""

import redis

import requests

from typing import Callable

_redis = redis.Redis()

def count_access(func: Callable) -> Callable:

    """

    Decorator function that counts the number of times a url was accessed

    """

    def wrapper(*args, **kwargs):

        key = "count:{}".format(args[0])

        _redis.incr(key)

        return func(*args, **kwargs)

    return wrapper

def get_cache(func: Callable) -> Callable:

    """

    Decorator function that caches the result of a url for 10 seconds

    """

    def wrapper(*args, **kwargs):

        key = "result:{}".format(args[0])

        if _redis.exists(key):

            return _redis.get(key).decode('utf-8')

        result = func(*args, **kwargs)

        _redis.set(key, result, ex=10)

        return result

    return wrapper

@get_cache

@count_access

def get_page(url: str) -> str:

    """

    Obtains the HTML content of a particular URL and returns it

    """

    response = requests.get(url)

    return response.text
