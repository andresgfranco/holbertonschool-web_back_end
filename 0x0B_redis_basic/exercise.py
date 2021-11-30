#!/usr/bin/env python3
"""This module contains the Cache class
"""

import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """counts each call of a function
    """
    key = method.__qualname__

    @wraps(method)
    def counter(self, *args, **kwargs):
        """increments the count the key every time the method is called
            and returns the value returned by the original method.
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return counter


def call_history(method: Callable) -> Callable:
    """stores the history of inputs and outputs for a particular function
    """
    @wraps(method)
    def save_input_output_history(self, *args, **kwargs):
        """saves the input and output of each function in redis
        """
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"

        output = method(self, *args, **kwargs)

        self._redis.rpush(input_key, str(args))
        self._redis.rpush(output_key, str(output))

        return output

    return save_input_output_history


def replay(method: Callable):
    """displays the history of calls of a particular function.
    """
    _redis = redis.Redis()

    fn_qname = method.__qualname__
    input_key = method.__qualname__ + ":inputs"
    output_key = method.__qualname__ + ":outputs"

    input_history = _redis.lrange(input_key, 0, -1)
    output_history = _redis.lrange(output_key, 0, -1)

    print("{} was called {} times:".format(fn_qname, len(input_history)))

    for i in list(zip(input_history, output_history)):
        print("{}(*{}) -> {}".format(
            fn_qname,
            i[0].decode(),
            i[1].decode())
        )


class Cache():
    """Cache class
    """
    def __init__(self):
        """Cache constructor
        """
        self._redis = redis.Redis()

        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """saves data in redis using an uniq uuid
        """
        new_key = str(uuid.uuid4())

        self._redis.set(new_key, data)

        return new_key

    def get(
        self,
        key: str,
        fn: Callable = None
    ) -> Union[str, bytes, int, float]:
        """gets data from redis and calls fn if is not None
            to format the data
        """
        data = self._redis.get(key)

        if fn:
            return fn(data)

        return data

    def get_str(self):
        """automatically parametrize Cache.get
            with the correct conversion function.
        """

    def get_int(self):
        """automatically parametrize Cache.get
            with the correct conversion function.
        """
