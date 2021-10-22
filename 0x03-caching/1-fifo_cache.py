#!/usr/bin/env python3
"""This module contains the class FIFOCache
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """inherits from BaseCaching and is a FIFO caching system"""
    __queue = []

    def put(self, key, item):
        """assigns to the dictionary self.cache_data
            the item value for the key key.
        """
        discard_key = ""

        if key is not None and item is not None:
            if key not in FIFOCache.__queue:
                if len(FIFOCache.__queue) == BaseCaching.MAX_ITEMS:
                    discard_key = FIFOCache.__queue[0]
                    FIFOCache.__queue.remove(discard_key)
                    self.cache_data.pop(discard_key, None)
                    print("DISCARD:", discard_key)

                FIFOCache.__queue.append(key)
            else:
                FIFOCache.__queue.remove(key)
                FIFOCache.__queue.append(key)

            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key.
        """
        if key is not None:
            return self.cache_data.get(key)
