#!/usr/bin/env python3
"""This module contains the class LRUCache
"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """inherits from BaseCaching and is a LRU caching system"""
    __lru_follow_up = {}
    __antiquity_value = 0

    def put(self, key, item):
        """assigns to the dictionary self.cache_data
            the item value for the key key.
        """
        if key is not None and item is not None:
            if key not in self.cache_data.keys():
                if len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS:
                    less_usage_value = None
                    less_usage_key = None
                    for k, v in LRUCache.__lru_follow_up.items():
                        if less_usage_value is None:
                            less_usage_value = v
                            less_usage_key = k

                        if v < less_usage_value:
                            less_usage_value = v
                            less_usage_key = k

                    self.cache_data.pop(less_usage_key, None)
                    LRUCache.__lru_follow_up.pop(less_usage_key, None)
                    print("DISCARD:", less_usage_key)

            self.cache_data[key] = item
            if key not in LRUCache.__lru_follow_up.keys():
                LRUCache.__lru_follow_up[key] = LRUCache.__antiquity_value
            LRUCache.__antiquity_value += 1

    def get(self, key):
        """return the value in self.cache_data linked to key.
        """
        if key is not None:
            if key in LRUCache.__lru_follow_up.keys():
                LRUCache.__lru_follow_up[key] = LRUCache.__antiquity_value
            LRUCache.__antiquity_value += 1
            return self.cache_data.get(key)
