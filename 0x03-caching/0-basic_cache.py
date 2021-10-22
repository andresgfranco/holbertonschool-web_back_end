#!/usr/bin/env python3
"""This module contains the class BasicCache
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """class BasicCache that inherits from BaseCaching
        and is a caching system
    """
    def put(self, key, item):
        """assigns to the dictionary self.cache_data
            the item value for the key key.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key.
        """
        if key is not None:
            return self.cache_data.get(key)
