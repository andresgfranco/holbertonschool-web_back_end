#!/usr/bin/env python3
"""This module contains the class LIFOCache
"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """inherits from BaseCaching and is a LIFO caching system"""
    __stack = []

    def put(self, key, item):
        """assigns to the dictionary self.cache_data
            the item value for the key key.
        """
        discard_key = ""

        if key is not None and item is not None:
            if key not in LIFOCache.__stack:
                if len(LIFOCache.__stack) == BaseCaching.MAX_ITEMS:
                    discard_key = LIFOCache.__stack[-1]
                    LIFOCache.__stack.remove(discard_key)
                    self.cache_data.pop(discard_key, None)
                    print("DISCARD:", discard_key)

                LIFOCache.__stack.append(key)
            else:
                LIFOCache.__stack.remove(key)
                LIFOCache.__stack.append(key)

            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key.
        """
        if key is not None:
            return self.cache_data.get(key)
