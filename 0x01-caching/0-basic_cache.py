#!/usr/bin/python3
"""  class BasicCache that inherits from BaseCaching
"""


BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class 
    """

    def put(self, key, item):
         
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
         
        return self.cache_data.get(key, None)
    