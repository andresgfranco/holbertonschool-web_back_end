#!/usr/bin/env python3
"""This module contains the class MRUCache
"""


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """inherits from BaseCaching and is a MRU caching system"""
    __lru_follow_up = {}
    __antiquity_value = 0

    def put(self, key, item):
        """assigns to the dictionary self.cache_data
            the item value for the key key.
        """
        if key is not None and item is not None:
            if key not in self.cache_data.keys():
                if len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS:
                    most_usage_value = None
                    most_usage_key = None
                    for k, v in MRUCache.__lru_follow_up.items():
                        if most_usage_value is None:
                            most_usage_value = v
                            most_usage_key = k

                        if v > most_usage_value:
                            most_usage_value = v
                            most_usage_key = k

                    self.cache_data.pop(most_usage_key, None)
                    MRUCache.__lru_follow_up.pop(most_usage_key, None)
                    print("DISCARD:", most_usage_key)

            self.cache_data[key] = item
            if key not in MRUCache.__lru_follow_up.keys():
                MRUCache.__lru_follow_up[key] = MRUCache.__antiquity_value
            MRUCache.__antiquity_value += 1

    def get(self, key):
        """return the value in self.cache_data linked to key.
        """
        if key is not None:
            if key in MRUCache.__lru_follow_up.keys():
                MRUCache.__lru_follow_up[key] = MRUCache.__antiquity_value
            MRUCache.__antiquity_value += 1
            return self.cache_data.get(key)
